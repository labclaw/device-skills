"""Tests for the BioTek Gen5 device skill."""

from __future__ import annotations

import csv
from pathlib import Path

import pytest
from devices.biotek_gen5 import Gen5Adapter, Gen5Brain, Gen5Processor
from devices.biotek_gen5.models import (
    PlateFormat,
    PlateReading,
    ReadingMode,
    Well,
    WellPlate,
)

from device_skills.schema import ControlMode

# ── Model tests ──────────────────────────────────────────────────────────


class TestWell:
    def test_name(self) -> None:
        w = Well(row="A", col=1, value=0.5)
        assert w.name == "A1"

    def test_name_double_digit(self) -> None:
        w = Well(row="H", col=12, value=0.1)
        assert w.name == "H12"

    def test_blank_corrected_default_none(self) -> None:
        w = Well(row="B", col=3, value=0.8)
        assert w.blank_corrected is None


class TestWellPlate:
    def _make_plate(self) -> WellPlate:
        return WellPlate(
            format=PlateFormat.PLATE_96,
            wells=[
                Well(row="A", col=1, value=1.0),
                Well(row="A", col=2, value=2.0),
                Well(row="B", col=1, value=3.0),
            ],
        )

    def test_get_well_found(self) -> None:
        plate = self._make_plate()
        assert plate.get_well("A2").value == 2.0  # type: ignore[union-attr]

    def test_get_well_missing(self) -> None:
        plate = self._make_plate()
        assert plate.get_well("Z9") is None

    def test_column(self) -> None:
        plate = self._make_plate()
        col1 = plate.column(1)
        assert len(col1) == 2
        assert all(w.col == 1 for w in col1)

    def test_row(self) -> None:
        plate = self._make_plate()
        row_a = plate.row("A")
        assert len(row_a) == 2


class TestPlateReading:
    def test_fields(self) -> None:
        plate = WellPlate(format=PlateFormat.PLATE_96)
        reading = PlateReading(plate=plate, mode=ReadingMode.ABSORBANCE, wavelength_nm=450)
        assert reading.wavelength_nm == 450
        assert reading.mode == ReadingMode.ABSORBANCE
        assert reading.protocol == ""
        assert reading.metadata == {}


# ── Adapter tests ────────────────────────────────────────────────────────


class TestGen5Adapter:
    def test_info(self) -> None:
        adapter = Gen5Adapter()
        info = adapter.info()
        assert info["name"] == "BioTek Gen5"
        assert info["vendor"] == "Agilent (BioTek)"
        assert info["type"] == "plate_reader"
        assert ControlMode.OFFLINE.value in info["supported_modes"]

    def test_connect_offline(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        assert adapter.connect() is True
        assert adapter.connected is True

    def test_disconnect(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        adapter.connect()
        adapter.disconnect()
        assert adapter.connected is False

    def test_mode_property(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        assert adapter.mode == ControlMode.OFFLINE

    def test_connect_api_returns_false(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.API)
        assert adapter.connect() is False
        assert adapter.connected is False

    def test_connect_gui_returns_false(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.GUI)
        assert adapter.connect() is False

    def test_list_datasets(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        adapter.connect()
        datasets = adapter.list_datasets()
        assert len(datasets) == 2
        assert any("ELISA" in d["name"] for d in datasets)
        assert any("Viability" in d["name"] for d in datasets)

    def test_process_elisa(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        adapter.connect()
        reading = adapter.process("ELISA_IL6_plate1")
        assert isinstance(reading, PlateReading)
        assert reading.mode == ReadingMode.ABSORBANCE
        assert reading.wavelength_nm == 450
        assert len(reading.plate.wells) == 96

    def test_process_viability(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        adapter.connect()
        reading = adapter.process("CellViability_DrugScreen")
        assert isinstance(reading, PlateReading)
        assert reading.mode == ReadingMode.FLUORESCENCE
        assert reading.wavelength_nm == 530

    def test_process_auto_connects(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        # Do not call connect() — should auto-connect
        reading = adapter.process("ELISA")
        assert adapter.connected is True
        assert isinstance(reading, PlateReading)

    def test_acquire_offline_raises(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        adapter.connect()
        with pytest.raises(RuntimeError, match="OFFLINE"):
            adapter.acquire()

    def test_blank_correction_applied(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        reading = adapter.process("ELISA")
        # All wells should have blank_corrected set
        for w in reading.plate.wells:
            assert w.blank_corrected is not None

    def test_blank_correction_math(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        reading = adapter.process("ELISA")
        blank_wells = [w for w in reading.plate.wells if w.col >= 11]
        blank_avg = sum(w.value for w in blank_wells) / len(blank_wells)
        sample = reading.plate.get_well("C5")
        assert sample is not None
        assert abs(sample.blank_corrected - (sample.value - blank_avg)) < 1e-3  # type: ignore[operator]

    def test_standard_higher_than_blank(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        reading = adapter.process("ELISA")
        blank = reading.plate.get_well("A12")
        standard = reading.plate.get_well("A1")
        assert standard is not None
        assert blank is not None
        assert standard.value > blank.value

    def test_csv_export(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        reading = adapter.process("ELISA")
        csv_text = Gen5Adapter.reading_to_csv(reading)
        assert "Protocol: ELISA Demo" in csv_text
        assert "Wavelength: 450nm" in csv_text
        lines = csv_text.strip().split("\n")
        assert len(lines) >= 10

    def test_list_datasets_raises_when_not_offline(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.API)
        adapter._connected = True  # force connected
        with pytest.raises(NotImplementedError):
            adapter.list_datasets()


# ── Processor tests ──────────────────────────────────────────────────────

def _write_gen5_csv(tmp_path: Path, wells: dict[str, float], metadata: dict[str, str]) -> Path:
    """Helper: write a minimal Gen5-style CSV to a temp file."""
    p = tmp_path / "plate.csv"
    with p.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        for k, v in metadata.items():
            writer.writerow([k, v])
        writer.writerow([])
        writer.writerow([""] + list(range(1, 13)))
        for row_letter in "ABCDEFGH":
            row_vals = [row_letter]
            for col in range(1, 13):
                row_vals.append(str(wells.get(f"{row_letter}{col}", 0.0)))
            writer.writerow(row_vals)
    return p


class TestGen5Processor:
    def test_load_parses_wells(self, tmp_path: Path) -> None:
        wells = {f"{r}{c}": float(i) for i, (r, c) in enumerate(
            (r, c) for r in "ABCDEFGH" for c in range(1, 13)
        )}
        csv_path = _write_gen5_csv(tmp_path, wells, {"Protocol": "Test", "Wavelength": "450nm"})

        processor = Gen5Processor()
        raw = processor.load(str(csv_path))
        assert "wells" in raw
        assert "metadata" in raw
        assert raw["metadata"]["Protocol"] == "Test"
        assert isinstance(raw["wells"]["A1"], float)

    def test_load_parses_96_wells(self, tmp_path: Path) -> None:
        wells = {f"{r}{c}": 0.5 for r in "ABCDEFGH" for c in range(1, 13)}
        csv_path = _write_gen5_csv(tmp_path, wells, {})
        processor = Gen5Processor()
        raw = processor.load(str(csv_path))
        assert len(raw["wells"]) == 96

    def test_transform_blank_correction(self, tmp_path: Path) -> None:
        # Blanks in cols 11-12 at 0.04, samples elsewhere at 1.0
        wells: dict[str, float] = {}
        for r in "ABCDEFGH":
            for c in range(1, 13):
                wells[f"{r}{c}"] = 0.04 if c >= 11 else 1.0

        csv_path = _write_gen5_csv(tmp_path, wells, {})
        processor = Gen5Processor()
        raw = processor.load(str(csv_path))
        corrected = processor.transform(raw)

        assert "blank_corrected" in corrected
        assert abs(corrected["blank_avg"] - 0.04) < 1e-6
        assert abs(corrected["blank_corrected"]["A1"] - (1.0 - 0.04)) < 1e-6

    def test_extract_returns_plate_reading(self, tmp_path: Path) -> None:
        wells = {f"{r}{c}": 0.5 for r in "ABCDEFGH" for c in range(1, 13)}
        csv_path = _write_gen5_csv(
            tmp_path, wells, {"Mode": "absorbance", "Wavelength": "450nm", "Protocol": "Test"}
        )
        processor = Gen5Processor()
        raw = processor.load(str(csv_path))
        corrected = processor.transform(raw)
        result = processor.extract(corrected)

        reading = result["reading"]
        assert isinstance(reading, PlateReading)
        assert reading.mode == ReadingMode.ABSORBANCE
        assert reading.wavelength_nm == 450
        assert len(reading.plate.wells) == 96

    def test_extract_stats(self, tmp_path: Path) -> None:
        wells = {f"{r}{c}": float(c) for r in "ABCDEFGH" for c in range(1, 13)}
        csv_path = _write_gen5_csv(tmp_path, wells, {})
        processor = Gen5Processor()
        raw = processor.load(str(csv_path))
        corrected = processor.transform(raw)
        result = processor.extract(corrected)

        stats = result["stats"]
        assert stats["well_count"] == 96
        assert "min" in stats
        assert "max" in stats
        assert "mean" in stats

    def test_extract_fluorescence_mode(self, tmp_path: Path) -> None:
        wells = {f"{r}{c}": 1000.0 for r in "ABCDEFGH" for c in range(1, 13)}
        csv_path = _write_gen5_csv(tmp_path, wells, {"Mode": "fluorescence", "Wavelength": "530"})
        processor = Gen5Processor()
        raw = processor.load(str(csv_path))
        corrected = processor.transform(raw)
        result = processor.extract(corrected)
        assert result["reading"].mode == ReadingMode.FLUORESCENCE
        assert result["reading"].wavelength_nm == 530


# ── Brain tests (cached, no API key required) ────────────────────────────


class TestGen5Brain:
    def test_interpret_elisa_cached(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        reading = adapter.process("ELISA")
        brain = Gen5Brain()

        analysis = brain.interpret_reading(reading, stream=False)
        assert isinstance(analysis, str)
        assert len(analysis) > 100
        assert "ELISA" in analysis

    def test_interpret_viability_cached(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        reading = adapter.process("CellViability")
        brain = Gen5Brain()

        analysis = brain.interpret_reading(reading, stream=False)
        assert isinstance(analysis, str)
        assert "viability" in analysis.lower() or "Viability" in analysis

    def test_interpret_streaming(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        reading = adapter.process("ELISA")
        brain = Gen5Brain()

        chunks = list(brain.interpret_reading(reading, stream=True))
        assert len(chunks) > 0
        full_text = "".join(chunks)
        assert "ELISA" in full_text

    def test_build_summary_contains_key_fields(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        reading = adapter.process("ELISA")
        brain = Gen5Brain()

        summary = brain._build_summary(reading)
        assert "Protocol:" in summary
        assert "Wavelength:" in summary
        assert "Signal/Noise:" in summary

    def test_analyze_with_reading(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        reading = adapter.process("ELISA")
        brain = Gen5Brain()

        result = brain.analyze({"reading": reading})
        assert isinstance(result, str)
        assert len(result) > 50

    def test_summarize_multiple_findings(self) -> None:
        brain = Gen5Brain()
        findings = ["Finding A: good signal.", "Finding B: no edge effects."]
        summary = brain.summarize(findings)
        assert isinstance(summary, str)
        assert len(summary) > 0

    def test_summarize_empty_findings(self) -> None:
        brain = Gen5Brain()
        result = brain.summarize([])
        assert "No findings" in result

    def test_unknown_protocol_raises_without_api(self) -> None:
        adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
        reading = adapter.process("ELISA")
        # Mutate protocol to something with no cache entry
        reading.protocol = "UnknownAssayXYZ"
        brain = Gen5Brain()

        if not brain._use_api:
            with pytest.raises(RuntimeError, match="No ANTHROPIC_API_KEY"):
                brain.interpret_reading(reading, stream=False)
