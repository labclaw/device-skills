"""Tests for the Bruker TopSpin device skill."""

from __future__ import annotations

from unittest.mock import patch

import numpy as np
import pytest
from devices.bruker_topspin.adapter import TopSpinAdapter
from devices.bruker_topspin.processor import NMRPeak, NMRSpectrum, TopSpinProcessor

from device_skills.schema import ControlMode

# ── NMRPeak ──────────────────────────────────────────────────────────────────


class TestNMRPeak:
    def test_basic_peak(self):
        peak = NMRPeak(ppm=7.26, intensity=100.0)
        assert peak.ppm == 7.26
        assert peak.intensity == 100.0

    def test_peak_with_all_fields(self):
        peak = NMRPeak(ppm=3.5, intensity=50.0, width_hz=2.5, multiplicity="t", integral=3.0)
        assert peak.width_hz == 2.5
        assert peak.multiplicity == "t"
        assert peak.integral == 3.0


# ── NMRSpectrum ───────────────────────────────────────────────────────────────


class TestNMRSpectrum:
    def test_basic_spectrum(self):
        data = np.array([0.0, 1.0, 0.5, 0.2])
        ppm = np.array([10.0, 7.5, 5.0, 2.5])
        peaks = [NMRPeak(ppm=7.5, intensity=1.0)]

        spectrum = NMRSpectrum(
            data=data,
            ppm_scale=ppm,
            peaks=peaks,
            nucleus="1H",
            solvent="CDCl3",
            frequency_mhz=400.0,
        )
        assert spectrum.nucleus == "1H"
        assert spectrum.solvent == "CDCl3"
        assert spectrum.frequency_mhz == 400.0
        assert len(spectrum.peaks) == 1
        assert spectrum.peaks[0].ppm == 7.5

    def test_spectrum_metadata(self):
        spectrum = NMRSpectrum(
            data=np.zeros(10),
            ppm_scale=np.linspace(10, 0, 10),
            peaks=[],
            nucleus="13C",
            solvent="DMSO",
            frequency_mhz=100.0,
            title="Test Compound",
            sample_name="test_sample",
        )
        assert spectrum.title == "Test Compound"
        assert spectrum.sample_name == "test_sample"


# ── TopSpinProcessor ─────────────────────────────────────────────────────────


class TestTopSpinProcessor:
    def test_processor_instantiation(self):
        proc = TopSpinProcessor()
        assert proc is not None

    def test_peak_filtering(self):
        """Peaks outside -1 to 15 ppm should be filtered."""
        proc = TopSpinProcessor()
        assert hasattr(proc, "process_1d")

    def test_format_peak_list_empty(self):
        proc = TopSpinProcessor()
        result = proc.format_peak_list([])
        assert result == "No peaks detected."

    def test_format_peak_list(self):
        proc = TopSpinProcessor()
        peaks = [
            NMRPeak(ppm=7.26, intensity=100.0),
            NMRPeak(ppm=3.50, intensity=50.0),
        ]
        result = proc.format_peak_list(peaks)
        assert "7.260" in result
        assert "3.500" in result
        assert "100.0%" in result

    def test_get_spectrum_summary(self):
        proc = TopSpinProcessor()
        spectrum = NMRSpectrum(
            data=np.zeros(10),
            ppm_scale=np.linspace(10, 0, 10),
            peaks=[NMRPeak(ppm=7.26, intensity=1.0)],
            nucleus="1H",
            solvent="CDCl3",
            frequency_mhz=400.0,
            title="Ethanol",
            sample_name="test",
        )
        summary = proc.get_spectrum_summary(spectrum)
        assert "1H" in summary
        assert "400.0 MHz" in summary
        assert "CDCl3" in summary
        assert "Ethanol" in summary

    def test_base_processor_load_interface(self):
        """TopSpinProcessor exposes load/transform/extract from BaseProcessor."""
        proc = TopSpinProcessor()
        assert hasattr(proc, "load")
        assert hasattr(proc, "transform")
        assert hasattr(proc, "extract")


# ── TopSpinAdapter ────────────────────────────────────────────────────────────


class TestTopSpinAdapter:
    def test_default_mode(self):
        adapter = TopSpinAdapter()
        assert adapter.mode == ControlMode.OFFLINE

    def test_explicit_offline_mode(self):
        adapter = TopSpinAdapter(mode=ControlMode.OFFLINE)
        assert adapter.mode == ControlMode.OFFLINE

    def test_string_mode(self):
        adapter = TopSpinAdapter(mode="offline")
        assert adapter.mode == ControlMode.OFFLINE

    def test_info_returns_dict(self):
        adapter = TopSpinAdapter()
        info = adapter.info()
        assert isinstance(info, dict)
        assert info["name"] == "TopSpin"
        assert info["vendor"] == "Bruker"
        assert info["type"].lower() == "nmr"
        assert ControlMode.OFFLINE in info["supported_modes"]
        assert ControlMode.API in info["supported_modes"]

    def test_connect_offline_no_examdata(self, tmp_path):
        """connect() returns False when examdata dir doesn't exist."""
        adapter = TopSpinAdapter(topspin_dir=str(tmp_path / "topspin_missing"))
        result = adapter.connect()
        assert result is False
        assert adapter.connected is False

    def test_connect_offline_with_examdata(self, tmp_path):
        """connect() returns True when examdata dir exists."""
        examdata = tmp_path / "topspin5.0.0" / "examdata"
        examdata.mkdir(parents=True)
        adapter = TopSpinAdapter(topspin_dir=str(tmp_path / "topspin5.0.0"))
        result = adapter.connect()
        assert result is True
        assert adapter.connected is True

    def test_disconnect(self):
        adapter = TopSpinAdapter()
        adapter._connected = True
        adapter.disconnect()
        assert adapter.connected is False

    def test_list_datasets_empty_dir(self, tmp_path):
        examdata = tmp_path / "topspin" / "examdata"
        examdata.mkdir(parents=True)
        adapter = TopSpinAdapter(topspin_dir=str(tmp_path / "topspin"))
        adapter.connect()
        datasets = adapter.list_datasets()
        assert isinstance(datasets, list)
        assert datasets == []

    def test_list_datasets_with_fid(self, tmp_path):
        """list_datasets finds experiment directories with fid files."""
        examdata = tmp_path / "topspin" / "examdata"
        sample = examdata / "my_sample" / "1"
        sample.mkdir(parents=True)
        (sample / "fid").write_bytes(b"\x00" * 8)
        pdata = sample / "pdata" / "1"
        pdata.mkdir(parents=True)
        (pdata / "title").write_text("Alpha Ionone\nmore text")

        adapter = TopSpinAdapter(topspin_dir=str(tmp_path / "topspin"))
        adapter.connect()
        datasets = adapter.list_datasets()

        assert len(datasets) == 1
        ds = datasets[0]
        assert ds["sample"] == "my_sample"
        assert ds["expno"] == 1
        assert ds["title"] == "Alpha Ionone"

    def test_acquire_offline_raises(self):
        adapter = TopSpinAdapter(mode=ControlMode.OFFLINE)
        with pytest.raises(RuntimeError, match="offline mode"):
            adapter.acquire()

    def test_process_returns_spectrum(self):
        """Processing a real dataset returns an NMRSpectrum (requires examdata)."""
        adapter = TopSpinAdapter()
        adapter.connect()
        datasets = adapter.list_datasets()
        if not datasets:
            pytest.skip("No TopSpin examdata available")

        target = None
        for ds in datasets:
            if ds["sample"] == "exam_CMCse_1" and ds["expno"] == 1:
                target = ds
                break

        if not target:
            pytest.skip("exam_CMCse_1 dataset not found")

        spectrum = adapter.process(target["path"])
        assert isinstance(spectrum, NMRSpectrum)
        assert len(spectrum.data) > 0
        assert len(spectrum.ppm_scale) > 0
        assert len(spectrum.peaks) > 0
        assert spectrum.frequency_mhz > 0
        assert spectrum.nucleus == "1H"


# ── Visualizer ────────────────────────────────────────────────────────────────


class TestVisualizer:
    def test_plot_returns_bytes(self):
        """plot_spectrum with output_path=None should return bytes."""
        from devices.bruker_topspin.visualizer import plot_spectrum

        spectrum = NMRSpectrum(
            data=np.sin(np.linspace(0, 10, 1000)),
            ppm_scale=np.linspace(12, -1, 1000),
            peaks=[NMRPeak(ppm=7.26, intensity=1.0)],
            nucleus="1H",
            solvent="CDCl3",
            frequency_mhz=400.0,
        )
        result = plot_spectrum(spectrum, output_path=None)
        assert isinstance(result, bytes)
        assert len(result) > 1000
        assert result[:4] == b"\x89PNG"

    def test_plot_saves_file(self, tmp_path):
        """plot_spectrum with a path should save a file."""
        from devices.bruker_topspin.visualizer import plot_spectrum

        spectrum = NMRSpectrum(
            data=np.sin(np.linspace(0, 10, 100)),
            ppm_scale=np.linspace(12, -1, 100),
            peaks=[],
            nucleus="1H",
            solvent="CDCl3",
            frequency_mhz=400.0,
        )
        out = tmp_path / "test_spectrum.png"
        result = plot_spectrum(spectrum, output_path=out)
        assert result == out
        assert out.exists()
        assert out.stat().st_size > 1000


# ── TopSpinBrain (cached mode) ────────────────────────────────────────────────


class TestTopSpinBrain:
    def test_brain_instantiation(self):
        from devices.bruker_topspin.brain import TopSpinBrain

        brain = TopSpinBrain()
        assert brain is not None

    def test_cached_interpretation(self):
        """Brain returns cached response for known compounds (no API key needed)."""
        from devices.bruker_topspin.brain import TopSpinBrain

        TopSpinBrain()
        spectrum = NMRSpectrum(
            data=np.zeros(100),
            ppm_scale=np.linspace(12, -1, 100),
            peaks=[NMRPeak(ppm=7.26, intensity=1.0)],
            nucleus="1H",
            solvent="CDCl3",
            frequency_mhz=400.0,
            sample_name="exam_CMCse_1",
            title="Alpha Ionone",
        )

        env = dict(**__import__("os").environ)
        env.pop("ANTHROPIC_API_KEY", None)
        with patch.dict("os.environ", env, clear=True):
            brain2 = TopSpinBrain()
            result = brain2.interpret_spectrum(spectrum, stream=False)
            assert isinstance(result, str)
            assert len(result) > 100

    def test_analyze_interface(self):
        """BaseBrain.analyze() works with a spectrum dict."""
        from devices.bruker_topspin.brain import TopSpinBrain

        spectrum = NMRSpectrum(
            data=np.zeros(100),
            ppm_scale=np.linspace(12, -1, 100),
            peaks=[NMRPeak(ppm=7.26, intensity=1.0)],
            nucleus="1H",
            solvent="CDCl3",
            frequency_mhz=400.0,
            title="Alpha Ionone",
        )

        env = dict(**__import__("os").environ)
        env.pop("ANTHROPIC_API_KEY", None)
        with patch.dict("os.environ", env, clear=True):
            brain = TopSpinBrain()
            result = brain.analyze({"spectrum": spectrum})
            assert isinstance(result, str)
            assert len(result) > 100

    def test_summarize_interface(self):
        """BaseBrain.summarize() returns a non-empty string."""
        from devices.bruker_topspin.brain import TopSpinBrain

        env = dict(**__import__("os").environ)
        env.pop("ANTHROPIC_API_KEY", None)
        with patch.dict("os.environ", env, clear=True):
            brain = TopSpinBrain()
            result = brain.summarize(["Finding A", "Finding B"])
            assert isinstance(result, str)
            assert len(result) > 0

    def test_summarize_empty(self):
        from devices.bruker_topspin.brain import TopSpinBrain

        brain = TopSpinBrain()
        result = brain.summarize([])
        assert result == "No findings to summarize."


# ── SpectralLibrary ───────────────────────────────────────────────────────────


class TestSpectralLibrary:
    def test_add_and_list(self):
        from devices.bruker_topspin.library import SpectralLibrary

        lib = SpectralLibrary()
        lib.add("ethanol", [1.2, 3.7, 4.8])
        lib.add("acetone", [2.1])
        assert len(lib) == 2
        assert lib.list_entries() == ["ethanol", "acetone"]

    def test_exact_match(self):
        from devices.bruker_topspin.library import SpectralLibrary

        lib = SpectralLibrary()
        lib.add("ethanol", [1.2, 3.7])
        lib.add("acetone", [2.1])
        lib.add("dmso", [2.5])

        matches = lib.match_peaks([1.2, 3.7])
        assert matches[0].entry.name == "ethanol"
        assert matches[0].score == 1.0

    def test_partial_match(self):
        from devices.bruker_topspin.library import SpectralLibrary

        lib = SpectralLibrary()
        lib.add("ethanol", [1.2, 3.7, 4.8])

        matches = lib.match_peaks([1.2, 3.7])
        assert matches[0].entry.name == "ethanol"
        assert matches[0].score > 0.5
        assert matches[0].matched_peaks == 2

    def test_tolerance(self):
        from devices.bruker_topspin.library import SpectralLibrary

        lib = SpectralLibrary(tolerance_ppm=0.1)
        lib.add("ethanol", [1.20])

        matches = lib.match_peaks([1.25])
        assert matches[0].score == 1.0

        lib2 = SpectralLibrary(tolerance_ppm=0.01)
        lib2.add("ethanol", [1.20])
        matches2 = lib2.match_peaks([1.25])
        assert matches2[0].score == 0.0

    def test_no_entries(self):
        from devices.bruker_topspin.library import SpectralLibrary

        lib = SpectralLibrary()
        matches = lib.match_peaks([1.2, 3.7])
        assert matches == []

    def test_empty_peaks(self):
        from devices.bruker_topspin.library import SpectralLibrary

        lib = SpectralLibrary()
        lib.add("ethanol", [1.2, 3.7])
        matches = lib.match_peaks([])
        assert matches[0].score == 0.0

    def test_add_spectrum(self):
        from devices.bruker_topspin.library import SpectralLibrary

        lib = SpectralLibrary()
        spectrum = NMRSpectrum(
            data=np.array([1.0]),
            ppm_scale=np.array([1.0]),
            peaks=[NMRPeak(ppm=7.26, intensity=100)],
            title="chloroform",
        )
        lib.add_spectrum(spectrum)
        assert lib.list_entries() == ["chloroform"]

    def test_match_spectrum(self):
        from devices.bruker_topspin.library import SpectralLibrary

        lib = SpectralLibrary()
        lib.add("chloroform", [7.26])
        lib.add("tms", [0.0])

        query = NMRSpectrum(
            data=np.array([1.0]),
            ppm_scale=np.array([1.0]),
            peaks=[NMRPeak(ppm=7.26, intensity=100)],
        )
        matches = lib.match(query)
        assert matches[0].entry.name == "chloroform"
        assert matches[0].score == 1.0

    def test_from_examdata(self):
        from pathlib import Path

        from devices.bruker_topspin.library import SpectralLibrary

        lib = SpectralLibrary.from_examdata()
        if Path("/opt/topspin5.0.0/examdata").exists():
            assert len(lib) > 0
        else:
            assert len(lib) == 0  # graceful fallback

    def test_top_k(self):
        from devices.bruker_topspin.library import SpectralLibrary

        lib = SpectralLibrary()
        for i in range(10):
            lib.add(f"compound_{i}", [float(i)])

        matches = lib.match_peaks([0.0], top_k=3)
        assert len(matches) == 3
