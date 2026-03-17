"""Two-photon imaging data processing — works offline without PrairieView.

Implements BaseProcessor (load -> transform -> extract) for Prairie View
OME-TIFF + XML data. Parses metadata from Prairie XML hierarchy, loads
image frames from OME-TIFF files, and produces ImagingStack objects.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np

from device_skills.base import BaseProcessor

logger = logging.getLogger(__name__)


@dataclass
class CalciumFrame:
    """Single imaging frame."""

    data: np.ndarray  # 2D array (height x width)
    timestamp: float  # Relative time in seconds
    channel: int = 1
    plane_index: int = 0


@dataclass
class ImagingStack:
    """Z-stack or time-series collection."""

    frames: list[CalciumFrame] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    num_channels: int = 1
    num_planes: int = 1
    frame_rate: float = 0.0
    pixels_per_line: int = 512
    lines_per_frame: int = 512
    microns_per_pixel_x: float = 0.0
    microns_per_pixel_y: float = 0.0
    objective: str = ""
    laser_wavelength: float = 0.0
    laser_power: float = 0.0
    scan_mode: str = ""  # "ResonantGalvo" or "Galvo"


@dataclass
class ROI:
    """Region of interest (detected cell)."""

    id: int
    x_center: float
    y_center: float
    mask: np.ndarray  # Binary mask
    trace: np.ndarray | None = None  # Fluorescence trace over time


def _safe_float(value: Any) -> float:
    """Convert a value to float, handling dicts (take first value) and errors."""
    if isinstance(value, dict):
        # IndexedValue — take the first numeric value
        for v in value.values():
            try:
                return float(v)
            except (ValueError, TypeError):
                continue
        return 0.0
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


def _safe_int(value: Any) -> int:
    """Convert a value to int, handling dicts and errors."""
    return int(_safe_float(value))


def _parse_prairie_xml(xml_path: Path) -> dict[str, Any]:
    """Parse a Prairie View XML metadata file.

    Handles the XML 1.1 vs 1.0 quirk: PrairieView writes ``<?xml version="1.1"?>``
    but Python's stdlib XML parser only supports 1.0.  We use lxml with
    ``recover=True`` to handle this gracefully.

    Args:
        xml_path: Path to the Prairie XML file.

    Returns:
        dict with parsed metadata keys.
    """
    from lxml import etree

    parser = etree.XMLParser(recover=True)
    tree = etree.parse(str(xml_path), parser)
    root = tree.getroot()

    meta: dict[str, Any] = {}
    meta["version"] = root.get("version", "")
    meta["date"] = root.get("date", "")
    meta["sequence_type"] = root.get("sequence_type", "")

    # Parse global PVStateShard values
    state_values = _parse_state_shard(root)
    meta.update(state_values)

    # Parse sequences and frames
    sequences: list[dict[str, Any]] = []
    for seq_elem in root.findall(".//Sequence"):
        seq_info: dict[str, Any] = {
            "type": seq_elem.get("type", ""),
            "cycle": int(seq_elem.get("cycle", "1")),
            "time": float(seq_elem.get("time", "0")),
        }

        frames: list[dict[str, Any]] = []
        for frame_elem in seq_elem.findall("Frame"):
            frame_info: dict[str, Any] = {
                "relative_time": float(frame_elem.get("relativeTime", "0")),
                "absolute_time": float(frame_elem.get("absoluteTime", "0")),
                "index": int(frame_elem.get("index", "0")),
            }
            files: list[dict[str, str]] = []
            for file_elem in frame_elem.findall("File"):
                files.append(
                    {
                        "channel": file_elem.get("channel", "1"),
                        "channel_name": file_elem.get("channelName", ""),
                        "filename": file_elem.get("filename", ""),
                    }
                )
            frame_info["files"] = files
            frames.append(frame_info)

        seq_info["frames"] = frames
        sequences.append(seq_info)

    meta["sequences"] = sequences
    return meta


def _parse_state_shard(element: Any) -> dict[str, Any]:
    """Extract PVStateValue entries from a PVStateShard element.

    Args:
        element: lxml element (PVScan root or Sequence or Frame).

    Returns:
        dict mapping parameter key -> value.
    """
    values: dict[str, Any] = {}
    for shard in element.findall("PVStateShard"):
        for sv in shard.findall("PVStateValue"):
            key = sv.get("key", "")
            value = sv.get("value", "")
            if key and value:
                values[key] = value
            # Handle IndexedValue sub-elements
            indexed = sv.findall("IndexedValue")
            if key and indexed:
                idx_values: dict[str, str] = {}
                for iv in indexed:
                    idx = iv.get("index", "")
                    val = iv.get("value", "")
                    if idx:
                        idx_values[idx] = val
                if idx_values:
                    values[key] = idx_values
    return values


def _load_tiff_frames(
    data_dir: Path,
    frame_files: list[dict[str, str]],
) -> list[np.ndarray]:
    """Load OME-TIFF frames from disk.

    Args:
        data_dir: Directory containing the TIFF files.
        frame_files: List of file info dicts with 'filename' key.

    Returns:
        List of 2D numpy arrays, one per file.
    """
    import tifffile

    arrays: list[np.ndarray] = []
    for finfo in frame_files:
        fname = finfo.get("filename", "")
        if not fname:
            continue
        fpath = data_dir / fname
        if fpath.exists():
            img = tifffile.imread(str(fpath))
            arrays.append(img)
        else:
            logger.warning("TIFF file not found, skipping: %s", fpath)
    return arrays


class TwoPhotonProcessor(BaseProcessor):
    """Process two-photon imaging data from Prairie View.

    Three-step pipeline: load -> transform -> extract.
    Works offline with OME-TIFF files and Prairie XML metadata.
    """

    def load(self, path: str) -> dict[str, Any]:
        """Load a Prairie data directory.

        Parses the XML metadata file and discovers OME-TIFF image files.

        Args:
            path: Path to the Prairie data directory containing XML + TIFFs.

        Returns:
            dict with 'metadata', 'data_dir', and 'tiff_files' keys.
        """
        data_dir = Path(path)
        if not data_dir.exists():
            raise FileNotFoundError(f"Data directory not found: {path}")
        if not data_dir.is_dir():
            raise ValueError(f"Path is not a directory: {path}")

        # Find the XML metadata file
        xml_files = list(data_dir.glob("*.xml"))
        if not xml_files:
            raise FileNotFoundError(f"No XML metadata file found in {path}")

        # Use the first XML file (typically one per acquisition)
        xml_path = xml_files[0]
        metadata = _parse_prairie_xml(xml_path)

        # Collect all TIFF filenames from the metadata
        tiff_files: list[dict[str, str]] = []
        for seq in metadata.get("sequences", []):
            for frame in seq.get("frames", []):
                tiff_files.extend(frame.get("files", []))

        return {
            "metadata": metadata,
            "data_dir": data_dir,
            "tiff_files": tiff_files,
        }

    def transform(self, raw_data: Any) -> ImagingStack:
        """Convert raw frames + metadata into an ImagingStack.

        Args:
            raw_data: dict as returned by load() with 'metadata', 'data_dir',
                      'tiff_files' keys.

        Returns:
            ImagingStack with frames and parsed metadata.
        """
        metadata: dict[str, Any] = raw_data["metadata"]
        data_dir: Path = raw_data["data_dir"]

        # Load TIFF frames
        frames: list[CalciumFrame] = []
        for seq in metadata.get("sequences", []):
            for frame_info in seq.get("frames", []):
                file_list = frame_info.get("files", [])
                arrays = _load_tiff_frames(data_dir, file_list)
                for i, arr in enumerate(arrays):
                    channel = int(file_list[i].get("channel", "1")) if i < len(file_list) else 1
                    frames.append(
                        CalciumFrame(
                            data=arr,
                            timestamp=frame_info.get("absolute_time", 0.0),
                            channel=channel,
                        )
                    )

        # Extract scan parameters from metadata
        # Some PVStateValues are IndexedValue dicts, others are flat strings.
        pixels_per_line = _safe_int(metadata.get("pixelsPerLine", 512))
        lines_per_frame = _safe_int(metadata.get("linesPerFrame", 512))

        # micronsPerPixel is stored as IndexedValue: {"XAxis": "0.87", "YAxis": "0.87"}
        microns_raw = metadata.get("micronsPerPixel", {})
        if isinstance(microns_raw, dict):
            microns_x = _safe_float(microns_raw.get("XAxis", 0))
            microns_y = _safe_float(microns_raw.get("YAxis", 0))
        else:
            microns_x = _safe_float(microns_raw)
            microns_y = microns_x

        objective = str(metadata.get("objectiveLens", ""))
        scan_mode = str(metadata.get("activeMode", metadata.get("scanMode", "")))

        # Laser info — may be indexed (multi-laser) or flat
        wl_raw = metadata.get("multiphotonWavelength", metadata.get("currentWavelength", 0))
        laser_wl = _safe_float(wl_raw)
        power_raw = metadata.get("laserPower", 0)
        laser_power = _safe_float(power_raw)

        # Compute frame rate from timing
        frame_rate = 0.0
        sequences = metadata.get("sequences", [])
        if sequences:
            all_frames = sequences[0].get("frames", [])
            if len(all_frames) >= 2:
                dt = all_frames[1].get("absolute_time", 0) - all_frames[0].get("absolute_time", 0)
                if dt > 0:
                    frame_rate = 1.0 / dt

        # Determine number of channels
        channels_seen: set[int] = set()
        for f in frames:
            channels_seen.add(f.channel)
        num_channels = max(len(channels_seen), 1)

        return ImagingStack(
            frames=frames,
            metadata=metadata,
            num_channels=num_channels,
            frame_rate=frame_rate,
            pixels_per_line=pixels_per_line,
            lines_per_frame=lines_per_frame,
            microns_per_pixel_x=microns_x,
            microns_per_pixel_y=microns_y,
            objective=objective,
            laser_wavelength=laser_wl,
            laser_power=laser_power,
            scan_mode=scan_mode,
        )

    def extract(self, processed_data: Any) -> dict[str, Any]:
        """Extract summary information from an ImagingStack.

        Args:
            processed_data: An ImagingStack instance.

        Returns:
            dict with frame count, dimensions, metadata, and max projection.
        """
        stack: ImagingStack = processed_data
        result: dict[str, Any] = {
            "num_frames": len(stack.frames),
            "num_channels": stack.num_channels,
            "num_planes": stack.num_planes,
            "frame_rate": stack.frame_rate,
            "pixels_per_line": stack.pixels_per_line,
            "lines_per_frame": stack.lines_per_frame,
            "microns_per_pixel_x": stack.microns_per_pixel_x,
            "microns_per_pixel_y": stack.microns_per_pixel_y,
            "objective": stack.objective,
            "laser_wavelength": stack.laser_wavelength,
            "laser_power": stack.laser_power,
            "scan_mode": stack.scan_mode,
        }

        # Compute max intensity projection if frames exist
        if stack.frames:
            result["max_projection"] = self.max_projection(stack)

        return result

    def max_projection(self, stack: ImagingStack, channel: int = 1) -> np.ndarray:
        """Compute max intensity projection across all frames for a channel.

        Args:
            stack: ImagingStack with frames.
            channel: Channel number to project (default 1).

        Returns:
            2D numpy array — max projection image.
        """
        channel_frames = [f.data for f in stack.frames if f.channel == channel]
        if not channel_frames:
            return np.zeros((stack.lines_per_frame, stack.pixels_per_line), dtype=np.uint16)
        return np.max(np.stack(channel_frames, axis=0), axis=0)

    def get_stack_summary(self, stack: ImagingStack) -> str:
        """Generate a text summary of the imaging stack for LLM context.

        Args:
            stack: ImagingStack to summarize.

        Returns:
            Human-readable summary string.
        """
        lines = [
            "Two-Photon Imaging Stack Summary",
            f"  Frames: {len(stack.frames)}",
            f"  Channels: {stack.num_channels}",
            f"  Planes: {stack.num_planes}",
            f"  Frame rate: {stack.frame_rate:.2f} Hz",
            f"  Resolution: {stack.pixels_per_line} x {stack.lines_per_frame}",
            f"  Pixel size: {stack.microns_per_pixel_x:.3f} x"
            f" {stack.microns_per_pixel_y:.3f} um/px",
            f"  Objective: {stack.objective}",
            f"  Laser: {stack.laser_wavelength:.0f} nm at {stack.laser_power:.1f} mW",
            f"  Scan mode: {stack.scan_mode}",
        ]
        return "\n".join(lines)
