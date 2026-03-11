"""Gen5Processor — data processing pipeline for BioTek Gen5 CSV exports.

Three-step pipeline:
  1. load(path)           — parse Gen5 CSV file into raw dict
  2. transform(raw_data)  — apply blank correction, validate wells
  3. extract(processed)   — return structured PlateReading result
"""

from __future__ import annotations

import csv
import logging
from pathlib import Path
from typing import Any

from device_skills.base import BaseProcessor

from .models import PlateFormat, PlateReading, ReadingMode, Well, WellPlate

logger = logging.getLogger(__name__)

# 96-well row letters (A–H) and column numbers (1–12)
_ROW_LETTERS = list("ABCDEFGH")
_COL_NUMBERS = list(range(1, 13))


class Gen5Processor(BaseProcessor):
    """Data processing pipeline for Gen5 CSV plate reader exports.

    Parses the Gen5 CSV format (metadata header rows + 8×12 grid),
    applies blank correction, and returns a structured PlateReading.

    Example::

        processor = Gen5Processor()
        raw = processor.load("data/elisa_plate1.csv")
        corrected = processor.transform(raw)
        result = processor.extract(corrected)
    """

    # -- BaseProcessor interface ------------------------------------------

    def load(self, path: str) -> dict[str, Any]:
        """Parse a Gen5 CSV export file.

        Expects CSV files where:
          - Leading rows without a recognised row letter are metadata.
          - Grid rows start with a row letter (A–H) followed by 12 numeric values.

        Args:
            path: Path to the CSV file.

        Returns:
            Dict with keys: wells (dict[str, float|str]), metadata (dict[str, str]),
            file (str).
        """
        file_path = Path(path)
        metadata: dict[str, str] = {}
        wells: dict[str, float | str] = {}

        with file_path.open(newline="", encoding="utf-8-sig") as fh:
            reader = csv.reader(fh)
            for raw_row in reader:
                if not raw_row:
                    continue

                first = raw_row[0].strip()

                if first.upper() in _ROW_LETTERS:
                    row_letter = first.upper()
                    values = raw_row[1:]
                    for col_idx, val in enumerate(values):
                        if col_idx >= len(_COL_NUMBERS):
                            break
                        col_num = _COL_NUMBERS[col_idx]
                        well_key = f"{row_letter}{col_num}"
                        stripped = val.strip()
                        try:
                            wells[well_key] = float(stripped)
                        except ValueError:
                            wells[well_key] = stripped
                else:
                    if len(raw_row) >= 2:
                        key = first
                        value = raw_row[1].strip()
                        if key:
                            metadata[key] = value

        logger.debug(
            "Gen5Processor loaded %d wells, %d metadata fields from %s",
            len(wells),
            len(metadata),
            file_path,
        )
        return {"wells": wells, "metadata": metadata, "file": str(file_path)}

    def transform(self, raw_data: dict[str, Any]) -> dict[str, Any]:
        """Apply blank correction to raw well data.

        Detects blank wells (columns 11–12) and subtracts their mean from all
        numeric well values. Non-numeric wells are left unchanged.

        Args:
            raw_data: Output from load() — dict with 'wells' and 'metadata'.

        Returns:
            Same structure as input with an added 'blank_corrected' key mapping
            well names to corrected float values.
        """
        wells: dict[str, float | str] = raw_data.get("wells", {})

        # Identify blank wells (columns 11–12)
        blank_values: list[float] = []
        for well_key, val in wells.items():
            if isinstance(val, float) and len(well_key) >= 2:
                col_str = well_key[1:]
                try:
                    col_num = int(col_str)
                    if col_num >= 11:
                        blank_values.append(val)
                except ValueError:
                    pass

        blank_avg = sum(blank_values) / len(blank_values) if blank_values else 0.0

        blank_corrected: dict[str, float] = {}
        for well_key, val in wells.items():
            if isinstance(val, float):
                blank_corrected[well_key] = round(val - blank_avg, 4)

        return {
            **raw_data,
            "blank_avg": blank_avg,
            "blank_corrected": blank_corrected,
        }

    def extract(self, processed_data: dict[str, Any]) -> dict[str, Any]:
        """Extract a structured PlateReading from processed data.

        Converts the flat well dict into a WellPlate with Well objects and
        returns a PlateReading plus summary statistics.

        Args:
            processed_data: Output from transform().

        Returns:
            Dict with keys: reading (PlateReading), stats (dict), file (str).
        """
        wells_raw: dict[str, float | str] = processed_data.get("wells", {})
        blank_corrected: dict[str, float] = processed_data.get("blank_corrected", {})
        metadata: dict[str, str] = processed_data.get("metadata", {})

        # Build Well objects
        well_objects: list[Well] = []
        for well_key, val in wells_raw.items():
            if not isinstance(val, float) or len(well_key) < 2:
                continue
            row_letter = well_key[0].upper()
            col_str = well_key[1:]
            try:
                col_num = int(col_str)
            except ValueError:
                continue

            corrected = blank_corrected.get(well_key)
            well_objects.append(
                Well(row=row_letter, col=col_num, value=val, blank_corrected=corrected)
            )

        # Sort wells for consistent ordering
        well_objects.sort(key=lambda w: (w.row, w.col))

        plate = WellPlate(format=PlateFormat.PLATE_96, wells=well_objects)

        # Infer reading mode from metadata
        mode_str = metadata.get("Mode", metadata.get("mode", "absorbance")).lower()
        try:
            mode = ReadingMode(mode_str)
        except ValueError:
            mode = ReadingMode.ABSORBANCE

        # Infer wavelength
        wavelength_str = metadata.get("Wavelength", metadata.get("wavelength", "450"))
        try:
            wavelength = int(wavelength_str.replace("nm", "").strip())
        except (ValueError, AttributeError):
            wavelength = 450

        protocol = metadata.get("Protocol", metadata.get("protocol", ""))

        reading = PlateReading(
            plate=plate,
            mode=mode,
            wavelength_nm=wavelength,
            protocol=protocol,
            metadata=dict(metadata),
        )

        # Basic statistics
        numeric_vals = [w.value for w in well_objects]
        stats: dict[str, Any] = {
            "well_count": len(well_objects),
            "blank_avg": processed_data.get("blank_avg", 0.0),
        }
        if numeric_vals:
            stats["min"] = min(numeric_vals)
            stats["max"] = max(numeric_vals)
            stats["mean"] = sum(numeric_vals) / len(numeric_vals)

        return {
            "reading": reading,
            "stats": stats,
            "file": processed_data.get("file", ""),
        }
