"""TopSpin NMR adapter — three control modes for the same instrument.

Control Modes:
  API:     gRPC to running TopSpin (port 3081) — fast, programmatic
  GUI:     Computer Use visual automation of TopSpin GUI — wow factor
  Offline: nmrglue processing, no TopSpin needed — works anywhere

All three modes produce the same NMRSpectrum output.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from device_skills.base import BaseAdapter
from device_skills.schema import ControlMode

from .processor import NMRSpectrum, TopSpinProcessor


class TopSpinAdapter(BaseAdapter):
    """Interface to TopSpin NMR software.

    Supports three control modes:
      - API: gRPC to running TopSpin (requires TopSpin GUI running)
      - GUI: Computer Use visual automation (requires TopSpin GUI visible)
      - Offline: nmrglue processing (no TopSpin needed at all)
    """

    def __init__(
        self,
        topspin_dir: str = "/opt/topspin5.0.0",
        mode: ControlMode | str = ControlMode.OFFLINE,
    ) -> None:
        self.topspin_dir = Path(topspin_dir)
        self.examdata_dir = self.topspin_dir / "examdata"
        self.processor = TopSpinProcessor()
        self._topspin = None
        self._dp = None
        self._gui = None
        self._connected = False
        self._mode = ControlMode(mode) if isinstance(mode, str) else mode

    def info(self) -> dict[str, Any]:
        return {
            "name": "TopSpin",
            "vendor": "Bruker",
            "type": "nmr",
            "supported_modes": [ControlMode.API, ControlMode.GUI, ControlMode.OFFLINE],
            "version": "5.0.0",
            "description": "Bruker TopSpin NMR acquisition and processing software",
        }

    @property
    def connected(self) -> bool:
        return self._connected

    @property
    def mode(self) -> ControlMode:
        return self._mode

    def connect(self) -> bool:
        """Try to connect based on current mode.

        For OFFLINE mode, always succeeds if examdata dir exists.
        For API mode, tries gRPC connection to TopSpin.
        For GUI mode, checks if TopSpin window is visible.
        """
        if self._mode == ControlMode.OFFLINE:
            self._connected = self.examdata_dir.exists()
            return self._connected

        if self._mode == ControlMode.API:
            return self._connect_api()

        if self._mode == ControlMode.GUI:
            return self._connect_gui()

        return False

    def disconnect(self) -> None:
        """Disconnect from the instrument."""
        self._connected = False
        self._topspin = None
        self._dp = None
        self._gui = None

    def _connect_api(self) -> bool:
        """Connect via gRPC to running TopSpin."""
        try:
            from bruker.api.topspin import Topspin

            self._topspin = Topspin()
            self._dp = self._topspin.getDataProvider()
            _ = self._topspin.getVersion()
            self._connected = True
            return True
        except Exception:
            self._connected = False
            return False

    def _connect_gui(self) -> bool:
        """Check if TopSpin GUI is visible for Computer Use."""
        try:
            from .gui_automation import TopSpinGUIAutomation

            self._gui = TopSpinGUIAutomation()
            if not self._gui.available:
                return False
            found = self._gui.detect_topspin_window()
            self._connected = found
            return found
        except Exception:
            self._connected = False
            return False

    def list_datasets(self) -> list[dict[str, Any]]:
        """List available example datasets."""
        return self._list_examdata()

    def _list_examdata(self) -> list[dict[str, Any]]:
        """List available example datasets from TopSpin examdata."""
        datasets = []
        if not self.examdata_dir.exists():
            return datasets
        for sample_dir in sorted(self.examdata_dir.iterdir()):
            if not sample_dir.is_dir():
                continue
            for expno_dir in sorted(sample_dir.iterdir()):
                if not expno_dir.is_dir() or not expno_dir.name.isdigit():
                    continue
                fid_path = expno_dir / "fid"
                if not fid_path.exists():
                    continue
                title = ""
                title_path = expno_dir / "pdata" / "1" / "title"
                if title_path.exists():
                    title = title_path.read_text().strip().split("\n")[0]
                datasets.append(
                    {
                        "path": str(expno_dir),
                        "sample": sample_dir.name,
                        "expno": int(expno_dir.name),
                        "title": title,
                    }
                )
        return datasets

    def acquire(self, **kwargs: Any) -> Any:
        """Acquire NMR data (start experiment).

        Only available in API and GUI modes — offline mode works
        with existing data only.
        """
        if self._mode == ControlMode.OFFLINE:
            raise RuntimeError("Cannot acquire data in offline mode")
        if self._mode == ControlMode.API:
            return self._acquire_api(**kwargs)
        if self._mode == ControlMode.GUI:
            return self._acquire_gui(**kwargs)

    def _acquire_api(self, **kwargs: Any) -> Any:
        """Start acquisition via gRPC API."""
        # TODO: Implement zg (acquire) via TopSpin API
        raise NotImplementedError("API acquisition not yet implemented")

    def _acquire_gui(self, **kwargs: Any) -> Any:
        """Start acquisition via Computer Use GUI automation."""
        # TODO: Click buttons in TopSpin GUI to start acquisition
        raise NotImplementedError("GUI acquisition not yet implemented")

    def process(self, data_path: str, **kwargs: Any) -> NMRSpectrum:
        """Process a dataset using the current control mode."""
        return self._process_dataset(data_path)

    def _process_dataset(self, dataset_path: str) -> NMRSpectrum:
        """Process a dataset — routes to the appropriate backend."""
        if self._mode == ControlMode.API and self._connected:
            return self._process_via_api(dataset_path)
        if self._mode == ControlMode.GUI and self._connected:
            return self._process_via_gui(dataset_path)
        # Offline mode (or fallback)
        return self._process_via_nmrglue(dataset_path)

    def _read_processed_pdata(
        self,
        dataset_path: str,
    ) -> NMRSpectrum:
        """Read already-processed pdata and pick peaks.

        Uses nmrglue to read the processed spectrum from pdata/1/
        instead of reprocessing the raw FID. Builds an NMRSpectrum
        and runs peak-picking only.
        """
        import nmrglue as ng
        import numpy as np

        path = Path(dataset_path)
        pdata_dir = path / "pdata" / "1"
        dic, data = ng.bruker.read_pdata(str(pdata_dir))

        # Read acquisition params for metadata
        acqu_dic, _ = ng.bruker.read(str(path))
        sf = acqu_dic["acqus"]["BF1"]
        solvent = acqu_dic["acqus"].get("SOLVENT", "unknown")

        # Build PPM scale from processed data
        udic = ng.bruker.guess_udic(acqu_dic, data)
        uc = ng.fileiobase.uc_from_udic(udic)
        ppm = uc.ppm_scale()

        # Metadata
        title = ""
        title_path = pdata_dir / "title"
        if title_path.exists():
            title = title_path.read_text().strip().split("\n")[0]
        sample_name = path.parent.name if path.exists() else ""

        spectrum = NMRSpectrum(
            data=np.real(data),
            ppm_scale=ppm,
            nucleus="1H",
            solvent=solvent,
            frequency_mhz=sf,
            title=title,
            sample_name=sample_name,
        )
        spectrum.peaks = self.processor.pick_peaks(spectrum)
        return spectrum

    def _process_via_nmrglue(self, dataset_path: str) -> NMRSpectrum:
        """Process using nmrglue (offline, no TopSpin needed)."""
        dic, fid = self.processor.read_bruker(dataset_path)
        return self.processor.process_1d(dic, fid, dataset_path=dataset_path)

    def _process_via_api(self, dataset_path: str) -> NMRSpectrum:
        """Process using TopSpin gRPC API (live).

        TopSpin handles FFT/phase/baseline via efp + apbk. We only
        read the already-processed pdata back via nmrglue — no need
        to redo the full pipeline. This is intentional for the MVP:
        TopSpin processing is preferred when available; nmrglue
        offline pipeline is the fallback.
        """
        nmrdata = self._dp.getNMRData(dataset_path)
        nmrdata.launch("efp")  # exponential multiply + FFT + phase
        nmrdata.launch("apbk -n")  # neural-net auto phase + baseline
        nmrdata.launch("ppf")  # peak picking
        # Read back already-processed pdata (not raw FID)
        return self._read_processed_pdata(dataset_path)

    def _process_via_gui(self, dataset_path: str) -> NMRSpectrum:
        """Process using Computer Use GUI automation.

        Visually operates the TopSpin GUI to run efp + apbk + ppf,
        then reads the already-processed pdata back. Same rationale
        as _process_via_api: TopSpin processing is preferred when
        available; nmrglue offline pipeline is the fallback.
        """
        self._gui.open_dataset(dataset_path)
        self._gui.process_spectrum()
        # Read back already-processed pdata (not raw FID)
        return self._read_processed_pdata(dataset_path)
