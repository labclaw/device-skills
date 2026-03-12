"""Two-photon microscope adapter — three control modes for the same instrument.

Control Modes:
  API:     PrairieLink COM/TCP to running PrairieView — fast, programmatic
  GUI:     Computer Use visual automation of PrairieView — wow factor
  Offline: OME-TIFF + XML processing, no PrairieView needed — works anywhere

All three modes produce the same ImagingStack output.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from device_skills.base import BaseAdapter
from device_skills.schema import ControlMode

from .processor import ImagingStack, TwoPhotonProcessor

# PrairieLink COM automation — Windows only
try:
    import win32com.client  # noqa: F401

    HAS_WIN32COM = True
except ImportError:
    HAS_WIN32COM = False

# Valid wavelength range for Ti:Sapphire laser
_MIN_WAVELENGTH_NM = 680
_MAX_WAVELENGTH_NM = 1080

# Default PrairieLink TCP port
_PRAIRIELINK_TCP_PORT = 1236


class TwoPhotonAdapter(BaseAdapter):
    """Interface to Bruker Ultima Investigator two-photon microscope.

    Supports three control modes:
      - API: PrairieLink COM/TCP to running PrairieView (Windows)
      - GUI: Computer Use visual automation (requires PrairieView visible)
      - Offline: OME-TIFF + XML processing (no PrairieView needed)
    """

    def __init__(
        self,
        data_dir: str = "",
        mode: ControlMode | str = ControlMode.OFFLINE,
    ) -> None:
        self._data_dir = Path(data_dir) if data_dir else Path.cwd()
        self._mode = ControlMode(mode) if isinstance(mode, str) else mode
        self._connected = False
        self._prairie_link: Any = None
        self.processor = TwoPhotonProcessor()

    def info(self) -> dict[str, Any]:
        return {
            "name": "Ultima Investigator",
            "vendor": "Bruker",
            "type": "two-photon-microscope",
            "supported_modes": [ControlMode.API, ControlMode.GUI, ControlMode.OFFLINE],
            "version": "5.x",
            "description": "Bruker Ultima Investigator two-photon fluorescence microscope",
        }

    @property
    def connected(self) -> bool:
        return self._connected

    @property
    def mode(self) -> ControlMode:
        return self._mode

    def connect(self) -> bool:
        """Connect based on current mode.

        Offline: always succeeds.
        API: requires PrairieLink COM or TCP on port 1236.
        GUI: requires PrairieView visible on screen.
        """
        if self._mode == ControlMode.OFFLINE:
            self._connected = True
            return True

        if self._mode == ControlMode.API:
            return self._connect_api()

        if self._mode == ControlMode.GUI:
            return self._connect_gui()

        return False

    def disconnect(self) -> None:
        """Disconnect from the instrument."""
        self._connected = False
        self._prairie_link = None

    def _connect_api(self) -> bool:
        """Connect via PrairieLink COM (Windows) or TCP."""
        if not HAS_WIN32COM:
            self._connected = False
            return False
        try:
            self._prairie_link = win32com.client.Dispatch(
                "PrairieLink64.Application"
            )
            self._prairie_link.Connect()
            self._connected = True
            return True
        except Exception:
            self._connected = False
            return False

    def _connect_gui(self) -> bool:
        """Check if PrairieView GUI is visible for Computer Use."""
        # GUI automation will be provided by device-use operator layer
        self._connected = False
        return False

    def list_datasets(self) -> list[dict[str, Any]]:
        """Scan data directory for Prairie acquisition directories.

        A Prairie dataset directory contains at least one XML metadata file
        and one or more OME-TIFF image files.

        Returns:
            List of dicts with 'path', 'name', 'xml_file', 'num_tiffs' keys.
        """
        datasets: list[dict[str, Any]] = []
        if not self._data_dir.exists():
            return datasets

        for child in sorted(self._data_dir.iterdir()):
            if not child.is_dir():
                continue
            xml_files = list(child.glob("*.xml"))
            tiff_files = list(child.glob("*.ome.tif")) + list(child.glob("*.tif"))
            if xml_files:
                datasets.append({
                    "path": str(child),
                    "name": child.name,
                    "xml_file": xml_files[0].name,
                    "num_tiffs": len(tiff_files),
                })
        return datasets

    def acquire(self, **kwargs: Any) -> Any:
        """Start an acquisition (API/GUI mode only).

        Offline mode cannot acquire — it processes existing data.

        Kwargs:
            mode: str — 'tseries', 'zseries', 'single', or 'linescan'.
        """
        if self._mode == ControlMode.OFFLINE:
            raise RuntimeError("Cannot acquire data in offline mode")
        if self._mode == ControlMode.API:
            return self._acquire_api(**kwargs)
        if self._mode == ControlMode.GUI:
            return self._acquire_gui(**kwargs)

    def _acquire_api(self, **kwargs: Any) -> Any:
        """Start acquisition via PrairieLink API."""
        acq_mode = kwargs.get("mode", "tseries")
        cmd_map = {
            "tseries": "-TSeries",
            "zseries": "-ZSeries",
            "single": "-SingleImage",
            "linescan": "-LineScan",
        }
        cmd = cmd_map.get(acq_mode, "-TSeries")
        if self._prairie_link is not None:
            self._prairie_link.SendScriptCommands(cmd)
        return {"status": "started", "mode": acq_mode}

    def _acquire_gui(self, **kwargs: Any) -> Any:
        """Start acquisition via Computer Use GUI automation."""
        raise NotImplementedError("GUI acquisition not yet implemented")

    def process(self, data_path: str, **kwargs: Any) -> ImagingStack:
        """Process a Prairie dataset directory into an ImagingStack.

        Args:
            data_path: Path to the directory containing XML + TIFFs.

        Returns:
            ImagingStack with all frames and metadata.
        """
        raw = self.processor.load(data_path)
        return self.processor.transform(raw)

    # ------------------------------------------------------------------
    # Two-photon specific methods
    # ------------------------------------------------------------------

    def get_motor_position(self) -> dict[str, float]:
        """Read current stage XYZ positions.

        Only available in API mode with active PrairieLink connection.

        Returns:
            dict with 'x', 'y', 'z' keys (in microns).

        Raises:
            RuntimeError: if not in API mode or not connected.
        """
        if self._mode != ControlMode.API or not self._connected:
            raise RuntimeError("Motor position requires API mode with active connection")
        if self._prairie_link is None:
            raise RuntimeError("PrairieLink not connected")
        x = float(self._prairie_link.GetMotorPosition("XAxis"))
        y = float(self._prairie_link.GetMotorPosition("YAxis"))
        z = float(self._prairie_link.GetMotorPosition("ZAxis"))
        return {"x": x, "y": y, "z": z}

    def set_motor_position(self, axis: str, position: float) -> bool:
        """Move a motor axis to a position.

        Args:
            axis: 'x', 'y', or 'z'.
            position: Target position in microns.

        Returns:
            True if command accepted.

        Raises:
            RuntimeError: if not in API mode or not connected.
        """
        if self._mode != ControlMode.API or not self._connected:
            raise RuntimeError("Motor control requires API mode with active connection")
        axis_map = {"x": "XAxis", "y": "YAxis", "z": "ZAxis"}
        pv_axis = axis_map.get(axis.lower())
        if pv_axis is None:
            raise ValueError(f"Invalid axis '{axis}'. Must be 'x', 'y', or 'z'.")
        if self._prairie_link is not None:
            self._prairie_link.SendScriptCommands(
                f"-SetMotorPosition {pv_axis} {position}"
            )
        return True

    def set_laser_wavelength(self, nm: float) -> bool:
        """Set the Ti:Sapphire laser wavelength.

        Args:
            nm: Wavelength in nanometers (680-1080 nm).

        Returns:
            True if command accepted.

        Raises:
            ValueError: if wavelength is outside valid range.
            RuntimeError: if not in API mode or not connected.
        """
        if nm < _MIN_WAVELENGTH_NM or nm > _MAX_WAVELENGTH_NM:
            raise ValueError(
                f"Wavelength {nm} nm outside valid range"
                f" ({_MIN_WAVELENGTH_NM}-{_MAX_WAVELENGTH_NM} nm)"
            )
        if self._mode != ControlMode.API or not self._connected:
            raise RuntimeError("Laser control requires API mode with active connection")
        if self._prairie_link is not None:
            self._prairie_link.SendScriptCommands(f"-SetLaserWavelength {nm:.0f}")
        return True

    def start_tseries(self) -> bool:
        """Start a T-series acquisition.

        Returns:
            True if command sent.

        Raises:
            RuntimeError: if not in API mode or not connected.
        """
        if self._mode != ControlMode.API or not self._connected:
            raise RuntimeError("Acquisition requires API mode with active connection")
        return self._acquire_api(mode="tseries") is not None

    def start_zseries(self) -> bool:
        """Start a Z-series acquisition.

        Returns:
            True if command sent.

        Raises:
            RuntimeError: if not in API mode or not connected.
        """
        if self._mode != ControlMode.API or not self._connected:
            raise RuntimeError("Acquisition requires API mode with active connection")
        return self._acquire_api(mode="zseries") is not None

    def abort(self) -> bool:
        """Abort the current acquisition.

        Returns:
            True if abort command sent.

        Raises:
            RuntimeError: if not in API mode or not connected.
        """
        if self._mode != ControlMode.API or not self._connected:
            raise RuntimeError("Abort requires API mode with active connection")
        if self._prairie_link is not None:
            self._prairie_link.SendScriptCommands("-Abort")
        return True
