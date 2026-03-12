"""BDD-style tests for the Bruker two-photon microscope device skill.

Given/When/Then naming convention. All external dependencies (tifffile,
lxml, win32com) are mocked — tests run without real Prairie data or Windows.
"""
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import numpy as np
import pytest
from devices.bruker_2p.adapter import TwoPhotonAdapter
from devices.bruker_2p.brain import TWO_PHOTON_SYSTEM_PROMPT, TwoPhotonBrain
from devices.bruker_2p.processor import (
    ROI,
    CalciumFrame,
    ImagingStack,
    TwoPhotonProcessor,
)

from device_skills.schema import ControlMode

# ── Fixtures ──────────────────────────────────────────────────────────────────


@pytest.fixture()
def sample_frame() -> CalciumFrame:
    """A 64x64 frame with random data."""
    return CalciumFrame(
        data=np.random.randint(0, 4096, (64, 64), dtype=np.uint16),
        timestamp=0.033,
        channel=1,
        plane_index=0,
    )


@pytest.fixture()
def sample_stack(sample_frame: CalciumFrame) -> ImagingStack:
    """Stack with 10 frames of 64x64 data."""
    frames = [
        CalciumFrame(
            data=np.random.randint(0, 4096, (64, 64), dtype=np.uint16),
            timestamp=i * 0.033,
            channel=1,
        )
        for i in range(10)
    ]
    return ImagingStack(
        frames=frames,
        metadata={"version": "5.6.64.400", "date": "2024-01-15"},
        num_channels=1,
        frame_rate=30.0,
        pixels_per_line=64,
        lines_per_frame=64,
        microns_per_pixel_x=0.8,
        microns_per_pixel_y=0.8,
        objective="16x/0.8 NA",
        laser_wavelength=920.0,
        laser_power=35.0,
        scan_mode="ResonantGalvo",
    )


@pytest.fixture()
def sample_rois() -> list[ROI]:
    """Three ROIs with fluorescence traces."""
    rois = []
    for i in range(3):
        trace = np.random.rand(300) * 100 + 500  # baseline ~500, noise ~100
        # Add calcium transients
        trace[50:55] += 300
        trace[150:155] += 250
        mask = np.zeros((64, 64), dtype=bool)
        mask[20 + i * 10 : 25 + i * 10, 30 + i * 5 : 35 + i * 5] = True
        rois.append(ROI(
            id=i + 1,
            x_center=32.0 + i * 5,
            y_center=22.0 + i * 10,
            mask=mask,
            trace=trace,
        ))
    return rois


# ── A. Data Classes ───────────────────────────────────────────────────────────


class TestCalciumFrame:
    """Given CalciumFrame data class, verify construction and defaults."""

    def test_calcium_frame_creation_with_defaults(self) -> None:
        """Given a 2D array and timestamp, When creating CalciumFrame, Then defaults apply."""
        data = np.zeros((512, 512), dtype=np.uint16)
        frame = CalciumFrame(data=data, timestamp=0.0)
        assert frame.channel == 1
        assert frame.plane_index == 0
        assert frame.data.shape == (512, 512)

    def test_calcium_frame_with_custom_channel(self) -> None:
        """Given channel=2, When creating CalciumFrame, Then channel is set."""
        frame = CalciumFrame(
            data=np.zeros((64, 64)),
            timestamp=1.5,
            channel=2,
            plane_index=3,
        )
        assert frame.channel == 2
        assert frame.plane_index == 3
        assert frame.timestamp == 1.5


class TestImagingStack:
    """Given ImagingStack data class, verify construction and metadata."""

    def test_imaging_stack_with_metadata(self, sample_stack: ImagingStack) -> None:
        """Given a populated stack, When accessing fields, Then metadata is correct."""
        assert len(sample_stack.frames) == 10
        assert sample_stack.num_channels == 1
        assert sample_stack.frame_rate == 30.0
        assert sample_stack.pixels_per_line == 64
        assert sample_stack.scan_mode == "ResonantGalvo"
        assert sample_stack.laser_wavelength == 920.0
        assert sample_stack.objective == "16x/0.8 NA"

    def test_imaging_stack_empty_defaults(self) -> None:
        """Given empty ImagingStack, When created with defaults, Then all zeros."""
        stack = ImagingStack()
        assert stack.frames == []
        assert stack.num_channels == 1
        assert stack.frame_rate == 0.0
        assert stack.scan_mode == ""


class TestROI:
    """Given ROI data class, verify trace association."""

    def test_roi_with_trace(self) -> None:
        """Given an ROI with a fluorescence trace, When accessed, Then trace is available."""
        trace = np.random.rand(100)
        mask = np.zeros((64, 64), dtype=bool)
        mask[10:15, 10:15] = True
        roi = ROI(id=1, x_center=12.5, y_center=12.5, mask=mask, trace=trace)
        assert roi.id == 1
        assert roi.trace is not None
        assert len(roi.trace) == 100

    def test_roi_without_trace(self) -> None:
        """Given an ROI without a trace, When accessed, Then trace is None."""
        mask = np.zeros((32, 32), dtype=bool)
        roi = ROI(id=5, x_center=16.0, y_center=16.0, mask=mask)
        assert roi.trace is None


# ── B. Processor ──────────────────────────────────────────────────────────────


class TestTwoPhotonProcessor:
    """Given TwoPhotonProcessor, verify load/transform/extract pipeline."""

    def test_processor_instantiation(self) -> None:
        """Given TwoPhotonProcessor, When instantiated, Then it has BaseProcessor methods."""
        proc = TwoPhotonProcessor()
        assert hasattr(proc, "load")
        assert hasattr(proc, "transform")
        assert hasattr(proc, "extract")

    def test_load_prairie_directory_parses_xml_metadata(self, tmp_path: Path) -> None:
        """Given a directory with XML + TIFF, When load(), Then metadata is parsed."""
        xml_content = b"""<?xml version="1.0"?>
<PVScan version="5.6.64.400" date="2024-01-15">
  <PVStateShard>
    <PVStateValue key="pixelsPerLine" value="512"/>
    <PVStateValue key="linesPerFrame" value="512"/>
  </PVStateShard>
  <Sequence type="TSeries" cycle="1" time="0.0">
    <Frame relativeTime="0.0" absoluteTime="0.0" index="1">
      <File channel="1" channelName="Ch1" filename="frame_001.ome.tif"/>
    </Frame>
    <Frame relativeTime="0.033" absoluteTime="0.033" index="2">
      <File channel="1" channelName="Ch1" filename="frame_002.ome.tif"/>
    </Frame>
  </Sequence>
</PVScan>"""
        data_dir = tmp_path / "TSeries-20240115-1200-001"
        data_dir.mkdir()
        (data_dir / "TSeries-20240115-1200-001.xml").write_bytes(xml_content)
        # Create dummy TIFF files
        (data_dir / "frame_001.ome.tif").write_bytes(b"\x00" * 8)
        (data_dir / "frame_002.ome.tif").write_bytes(b"\x00" * 8)

        proc = TwoPhotonProcessor()
        result = proc.load(str(data_dir))

        assert "metadata" in result
        assert result["metadata"]["version"] == "5.6.64.400"
        assert result["metadata"]["pixelsPerLine"] == "512"
        assert len(result["tiff_files"]) == 2

    def test_load_handles_xml_v1_v1_1_quirk(self, tmp_path: Path) -> None:
        """Given XML 1.1 header (PrairieView quirk), When load(), Then parsing succeeds."""
        xml_content = b"""<?xml version="1.1"?>
<PVScan version="5.6.64.400">
  <Sequence type="TSeries" cycle="1" time="0.0">
    <Frame relativeTime="0.0" absoluteTime="0.0" index="1">
      <File channel="1" channelName="Ch1" filename="img.ome.tif"/>
    </Frame>
  </Sequence>
</PVScan>"""
        data_dir = tmp_path / "data"
        data_dir.mkdir()
        (data_dir / "meta.xml").write_bytes(xml_content)

        proc = TwoPhotonProcessor()
        result = proc.load(str(data_dir))
        assert result["metadata"]["version"] == "5.6.64.400"

    def test_transform_creates_imaging_stack_from_raw(self, tmp_path: Path) -> None:
        """Given raw load output with TIFFs, When transform(), Then ImagingStack is created."""
        data_dir = tmp_path / "data"
        data_dir.mkdir()

        # Create a real small TIFF
        import tifffile

        frame_data = np.random.randint(0, 4096, (64, 64), dtype=np.uint16)
        tifffile.imwrite(str(data_dir / "frame.ome.tif"), frame_data)

        raw = {
            "metadata": {
                "version": "5.6",
                "sequences": [{
                    "type": "TSeries",
                    "cycle": 1,
                    "time": 0.0,
                    "frames": [{
                        "relative_time": 0.0,
                        "absolute_time": 0.0,
                        "index": 1,
                        "files": [
                            {"channel": "1", "channel_name": "Ch1",
                             "filename": "frame.ome.tif"},
                        ],
                    }],
                }],
            },
            "data_dir": data_dir,
            "tiff_files": [{"channel": "1", "filename": "frame.ome.tif"}],
        }

        proc = TwoPhotonProcessor()
        stack = proc.transform(raw)

        assert isinstance(stack, ImagingStack)
        assert len(stack.frames) == 1
        assert stack.frames[0].data.shape == (64, 64)

    def test_extract_produces_summary_dict(self, sample_stack: ImagingStack) -> None:
        """Given an ImagingStack, When extract(), Then summary dict is returned."""
        proc = TwoPhotonProcessor()
        result = proc.extract(sample_stack)

        assert result["num_frames"] == 10
        assert result["num_channels"] == 1
        assert result["frame_rate"] == 30.0
        assert result["scan_mode"] == "ResonantGalvo"
        assert "max_projection" in result

    def test_max_projection_calculation(self, sample_stack: ImagingStack) -> None:
        """Given a stack with frames, When max_projection(), Then max across frames."""
        proc = TwoPhotonProcessor()
        proj = proc.max_projection(sample_stack, channel=1)

        assert proj.shape == (64, 64)
        # Max projection should be >= any individual frame at every pixel
        for f in sample_stack.frames:
            assert np.all(proj >= f.data)

    def test_processor_handles_missing_directory(self) -> None:
        """Given a non-existent path, When load(), Then FileNotFoundError."""
        proc = TwoPhotonProcessor()
        with pytest.raises(FileNotFoundError):
            proc.load("/nonexistent/path")

    def test_processor_handles_empty_directory(self, tmp_path: Path) -> None:
        """Given a directory without XML, When load(), Then FileNotFoundError."""
        empty_dir = tmp_path / "empty"
        empty_dir.mkdir()
        proc = TwoPhotonProcessor()
        with pytest.raises(FileNotFoundError, match="No XML"):
            proc.load(str(empty_dir))

    def test_processor_multiplane_data(self) -> None:
        """Given frames across multiple planes, When max_projection(channel=2), Then filtered."""
        frames = [
            CalciumFrame(data=np.ones((32, 32), dtype=np.uint16) * 100, timestamp=0.0, channel=1),
            CalciumFrame(data=np.ones((32, 32), dtype=np.uint16) * 200, timestamp=0.0, channel=2),
        ]
        stack = ImagingStack(frames=frames, num_channels=2, pixels_per_line=32, lines_per_frame=32)
        proc = TwoPhotonProcessor()

        proj_ch1 = proc.max_projection(stack, channel=1)
        proj_ch2 = proc.max_projection(stack, channel=2)

        assert np.all(proj_ch1 == 100)
        assert np.all(proj_ch2 == 200)

    def test_get_stack_summary(self, sample_stack: ImagingStack) -> None:
        """Given a stack, When get_stack_summary(), Then readable text is returned."""
        proc = TwoPhotonProcessor()
        summary = proc.get_stack_summary(sample_stack)

        assert "Two-Photon Imaging Stack Summary" in summary
        assert "920 nm" in summary
        assert "ResonantGalvo" in summary
        assert "30.00 Hz" in summary


# ── C. Adapter ────────────────────────────────────────────────────────────────


class TestTwoPhotonAdapter:
    """Given TwoPhotonAdapter, verify control modes and operations."""

    def test_adapter_offline_connect_succeeds(self) -> None:
        """Given offline mode, When connect(), Then returns True."""
        adapter = TwoPhotonAdapter(mode=ControlMode.OFFLINE)
        assert adapter.connect() is True
        assert adapter.connected is True

    def test_adapter_api_mode_requires_win32com(self) -> None:
        """Given API mode without win32com, When connect(), Then returns False."""
        adapter = TwoPhotonAdapter(mode=ControlMode.API)
        # On macOS/Linux, win32com is not available
        result = adapter.connect()
        # If HAS_WIN32COM is False, should fail gracefully
        if not adapter._prairie_link:
            assert result is False

    def test_adapter_default_mode_is_offline(self) -> None:
        """Given no mode specified, When creating adapter, Then mode is OFFLINE."""
        adapter = TwoPhotonAdapter()
        assert adapter.mode == ControlMode.OFFLINE

    def test_adapter_string_mode(self) -> None:
        """Given mode as string, When creating adapter, Then mode enum is set."""
        adapter = TwoPhotonAdapter(mode="offline")
        assert adapter.mode == ControlMode.OFFLINE

    def test_adapter_list_datasets_finds_prairie_dirs(self, tmp_path: Path) -> None:
        """Given a directory with Prairie datasets, When list_datasets(), Then found."""
        # Create two Prairie dataset directories
        ds1 = tmp_path / "TSeries-20240115-001"
        ds1.mkdir()
        (ds1 / "TSeries-20240115-001.xml").write_bytes(b"<PVScan/>")
        (ds1 / "frame_001.ome.tif").write_bytes(b"\x00" * 8)

        ds2 = tmp_path / "ZSeries-20240115-002"
        ds2.mkdir()
        (ds2 / "ZSeries-20240115-002.xml").write_bytes(b"<PVScan/>")

        adapter = TwoPhotonAdapter(data_dir=str(tmp_path), mode=ControlMode.OFFLINE)
        adapter.connect()
        datasets = adapter.list_datasets()

        assert len(datasets) == 2
        assert datasets[0]["name"] == "TSeries-20240115-001"
        assert datasets[0]["num_tiffs"] == 1

    def test_adapter_list_datasets_empty_dir(self, tmp_path: Path) -> None:
        """Given an empty directory, When list_datasets(), Then empty list."""
        adapter = TwoPhotonAdapter(data_dir=str(tmp_path))
        assert adapter.list_datasets() == []

    def test_adapter_process_routes_to_processor(self, tmp_path: Path) -> None:
        """Given a data path, When process(), Then processor is called."""
        adapter = TwoPhotonAdapter(mode=ControlMode.OFFLINE)
        adapter.connect()

        mock_stack = ImagingStack(frames=[], metadata={})
        load_rv = {
            "metadata": {}, "data_dir": tmp_path, "tiff_files": [],
        }
        with patch.object(adapter.processor, "load", return_value=load_rv), \
             patch.object(adapter.processor, "transform", return_value=mock_stack):
            result = adapter.process(str(tmp_path))
            assert isinstance(result, ImagingStack)

    def test_adapter_get_motor_position_offline_raises(self) -> None:
        """Given offline mode, When get_motor_position(), Then RuntimeError."""
        adapter = TwoPhotonAdapter(mode=ControlMode.OFFLINE)
        adapter.connect()
        with pytest.raises(RuntimeError, match="API mode"):
            adapter.get_motor_position()

    def test_adapter_set_laser_wavelength_validates_range(self) -> None:
        """Given wavelength outside 680-1080 nm, When set_laser_wavelength(), Then ValueError."""
        adapter = TwoPhotonAdapter(mode=ControlMode.OFFLINE)
        with pytest.raises(ValueError, match="outside valid range"):
            adapter.set_laser_wavelength(500.0)
        with pytest.raises(ValueError, match="outside valid range"):
            adapter.set_laser_wavelength(1200.0)

    def test_adapter_disconnect_cleans_up(self) -> None:
        """Given a connected adapter, When disconnect(), Then state is reset."""
        adapter = TwoPhotonAdapter(mode=ControlMode.OFFLINE)
        adapter.connect()
        assert adapter.connected is True
        adapter.disconnect()
        assert adapter.connected is False
        assert adapter._prairie_link is None

    def test_adapter_info_returns_metadata(self) -> None:
        """Given any adapter, When info(), Then instrument metadata is returned."""
        adapter = TwoPhotonAdapter()
        info = adapter.info()
        assert info["name"] == "Ultima Investigator"
        assert info["vendor"] == "Bruker"
        assert info["type"] == "two-photon-microscope"
        assert ControlMode.OFFLINE in info["supported_modes"]
        assert ControlMode.API in info["supported_modes"]

    def test_adapter_acquire_offline_raises(self) -> None:
        """Given offline mode, When acquire(), Then RuntimeError."""
        adapter = TwoPhotonAdapter(mode=ControlMode.OFFLINE)
        with pytest.raises(RuntimeError, match="offline mode"):
            adapter.acquire()


# ── D. Driver ─────────────────────────────────────────────────────────────────


class TestTwoPhotonDriver:
    """Given TwoPhotonDriver, verify labclaw contract."""

    def test_driver_device_type(self) -> None:
        """Given a driver, When device_type, Then 'two-photon-microscope'."""
        from devices.bruker_2p.driver import TwoPhotonDriver

        driver = TwoPhotonDriver()
        assert driver.device_type == "two-photon-microscope"

    def test_driver_device_id_default(self) -> None:
        """Given no device_id, When created, Then default ID is used."""
        from devices.bruker_2p.driver import TwoPhotonDriver

        driver = TwoPhotonDriver()
        assert driver.device_id == "bruker-2p-001"

    @pytest.mark.asyncio
    async def test_driver_connect_offline(self) -> None:
        """Given offline mode, When connect(), Then succeeds."""
        from devices.bruker_2p.driver import TwoPhotonDriver

        driver = TwoPhotonDriver(config={"mode": "offline"})
        result = await driver.connect()
        assert result is True
        assert driver._connected is True

    @pytest.mark.asyncio
    async def test_driver_read_returns_error_without_data(self) -> None:
        """Given connected driver with no data, When read(), Then error dict."""
        from devices.bruker_2p.driver import TwoPhotonDriver

        driver = TwoPhotonDriver()
        await driver.connect()
        result = await driver.read()
        assert "error" in result

    @pytest.mark.asyncio
    async def test_driver_read_not_connected(self) -> None:
        """Given unconnected driver, When read(), Then error dict."""
        from devices.bruker_2p.driver import TwoPhotonDriver

        driver = TwoPhotonDriver()
        result = await driver.read()
        assert result == {"error": "Not connected"}

    @pytest.mark.asyncio
    async def test_driver_write_processes_command(self) -> None:
        """Given connected driver, When write(process), Then delegates to adapter."""
        from devices.bruker_2p.driver import TwoPhotonDriver

        driver = TwoPhotonDriver()
        await driver.connect()

        mock_stack = ImagingStack(
            frames=[CalciumFrame(data=np.zeros((64, 64)), timestamp=0.0)],
            metadata={},
            scan_mode="ResonantGalvo",
            laser_wavelength=920.0,
        )
        with patch.object(driver._adapter, "process", return_value=mock_stack):
            result = await driver.write({"action": "process", "path": "/some/path"})
            assert result is True
            read_result = await driver.read()
            assert read_result["num_frames"] == 1
            assert read_result["scan_mode"] == "ResonantGalvo"

    @pytest.mark.asyncio
    async def test_driver_disconnect(self) -> None:
        """Given connected driver, When disconnect(), Then not connected."""
        from devices.bruker_2p.driver import TwoPhotonDriver

        driver = TwoPhotonDriver()
        await driver.connect()
        await driver.disconnect()
        assert driver._connected is False
        assert driver._adapter is None

    def test_driver_info(self) -> None:
        """Given a driver, When info(), Then metadata dict is returned."""
        from devices.bruker_2p.driver import TwoPhotonDriver

        driver = TwoPhotonDriver(device_id="test-2p")
        info = driver.info()
        assert info["device_id"] == "test-2p"
        assert info["device_type"] == "two-photon-microscope"
        assert info["mode"] == "offline"


# ── E. Brain ──────────────────────────────────────────────────────────────────


class TestTwoPhotonBrain:
    """Given TwoPhotonBrain, verify analysis and demo cache fallback."""

    def test_brain_instantiation(self) -> None:
        """Given no API key, When creating brain, Then no error."""
        env = dict(**__import__("os").environ)
        env.pop("ANTHROPIC_API_KEY", None)
        with patch.dict("os.environ", env, clear=True):
            brain = TwoPhotonBrain()
            assert brain.client is None

    def test_brain_analyze_returns_interpretation(
        self, sample_stack: ImagingStack,
    ) -> None:
        """Given a stack, When analyze(), Then cached demo response is returned."""
        env = dict(**__import__("os").environ)
        env.pop("ANTHROPIC_API_KEY", None)
        with patch.dict("os.environ", env, clear=True):
            brain = TwoPhotonBrain()
            result = brain.analyze({"stack": sample_stack})
            assert isinstance(result, str)
            assert "Image Quality" in result

    def test_brain_summarize_combines_findings(self) -> None:
        """Given multiple findings, When summarize(), Then combined text."""
        env = dict(**__import__("os").environ)
        env.pop("ANTHROPIC_API_KEY", None)
        with patch.dict("os.environ", env, clear=True):
            brain = TwoPhotonBrain()
            result = brain.summarize(["Finding A", "Finding B"])
            assert "Finding A" in result
            assert "Finding B" in result
            assert "2 imaging findings" in result

    def test_brain_summarize_empty(self) -> None:
        """Given no findings, When summarize(), Then message returned."""
        brain = TwoPhotonBrain()
        assert brain.summarize([]) == "No findings to summarize."

    def test_brain_suggest_params_for_gcamp(self) -> None:
        """Given GCaMP context, When suggest_imaging_params(), Then GCaMP-specific advice."""
        env = dict(**__import__("os").environ)
        env.pop("ANTHROPIC_API_KEY", None)
        with patch.dict("os.environ", env, clear=True):
            brain = TwoPhotonBrain()
            result = brain.suggest_imaging_params(context="GCaMP6f in V1 cortex")
            assert "920 nm" in result
            assert "GCaMP" in result

    def test_brain_offline_uses_demo_cache(self) -> None:
        """Given no API key, When analyze(), Then demo cache is used (not API)."""
        env = dict(**__import__("os").environ)
        env.pop("ANTHROPIC_API_KEY", None)
        with patch.dict("os.environ", env, clear=True):
            brain = TwoPhotonBrain()
            assert brain._use_api is False
            result = brain.analyze({"summary": "test data"})
            assert len(result) > 100

    def test_brain_system_prompt_includes_2p_expertise(self) -> None:
        """Given the system prompt, Then it includes two-photon domain knowledge."""
        assert "two-photon" in TWO_PHOTON_SYSTEM_PROMPT.lower()
        assert "calcium" in TWO_PHOTON_SYSTEM_PROMPT.lower()
        assert "photobleaching" in TWO_PHOTON_SYSTEM_PROMPT.lower()
        assert "GCaMP" in TWO_PHOTON_SYSTEM_PROMPT

    def test_brain_compare_sessions_offline(self) -> None:
        """Given no API key, When compare_sessions(), Then demo cache response."""
        env = dict(**__import__("os").environ)
        env.pop("ANTHROPIC_API_KEY", None)
        with patch.dict("os.environ", env, clear=True):
            brain = TwoPhotonBrain()
            result = brain.compare_sessions(
                {"session": 1, "date": "2024-01-15"},
                {"session": 2, "date": "2024-01-16"},
            )
            assert "registration" in result.lower()

    def test_brain_interpret_activity_with_rois(
        self, sample_stack: ImagingStack, sample_rois: list[ROI],
    ) -> None:
        """Given stack + ROIs, When interpret_activity(), Then analysis returned."""
        env = dict(**__import__("os").environ)
        env.pop("ANTHROPIC_API_KEY", None)
        with patch.dict("os.environ", env, clear=True):
            brain = TwoPhotonBrain()
            result = brain.interpret_activity(sample_stack, rois=sample_rois)
            assert isinstance(result, str)
            assert len(result) > 100


# ── F. Visualizer ─────────────────────────────────────────────────────────────


class TestVisualizer:
    """Given visualizer functions, verify plot generation."""

    def test_plot_max_projection_creates_figure(
        self, sample_stack: ImagingStack,
    ) -> None:
        """Given a stack, When plot_max_projection(output_path=None), Then PNG bytes."""
        from devices.bruker_2p.visualizer import plot_max_projection

        result = plot_max_projection(sample_stack, output_path=None)
        assert isinstance(result, bytes)
        assert len(result) > 1000
        assert result[:4] == b"\x89PNG"

    def test_plot_max_projection_saves_file(
        self, sample_stack: ImagingStack, tmp_path: Path,
    ) -> None:
        """Given output_path, When plot_max_projection(), Then file is saved."""
        from devices.bruker_2p.visualizer import plot_max_projection

        out = tmp_path / "test_proj.png"
        result = plot_max_projection(sample_stack, output_path=out)
        assert result == out
        assert out.exists()
        assert out.stat().st_size > 1000

    def test_plot_fov_overlay_accepts_two_images(self) -> None:
        """Given two images, When plot_fov_overlay(), Then composite PNG bytes."""
        from devices.bruker_2p.visualizer import plot_fov_overlay

        ref = np.random.randint(0, 4096, (64, 64), dtype=np.uint16)
        cur = np.random.randint(0, 4096, (64, 64), dtype=np.uint16)
        result = plot_fov_overlay(ref, cur, output_path=None)
        assert isinstance(result, bytes)
        assert result[:4] == b"\x89PNG"

    def test_plot_fov_overlay_different_sizes(self) -> None:
        """Given images of different sizes, When plot_fov_overlay(), Then crops to smaller."""
        from devices.bruker_2p.visualizer import plot_fov_overlay

        ref = np.zeros((64, 64), dtype=np.uint16)
        cur = np.zeros((32, 48), dtype=np.uint16)
        result = plot_fov_overlay(ref, cur, output_path=None)
        assert isinstance(result, bytes)

    def test_plot_calcium_traces_with_rois(self, sample_rois: list[ROI]) -> None:
        """Given ROIs with traces, When plot_calcium_traces(), Then PNG bytes."""
        from devices.bruker_2p.visualizer import plot_calcium_traces

        result = plot_calcium_traces(sample_rois, frame_rate=30.0, output_path=None)
        assert isinstance(result, bytes)
        assert result[:4] == b"\x89PNG"

    def test_plot_calcium_traces_empty(self) -> None:
        """Given no ROIs, When plot_calcium_traces(), Then still produces figure."""
        from devices.bruker_2p.visualizer import plot_calcium_traces

        result = plot_calcium_traces([], frame_rate=30.0, output_path=None)
        assert isinstance(result, bytes)
        assert result[:4] == b"\x89PNG"

    def test_plot_handles_empty_data(self) -> None:
        """Given empty stack, When plot_max_projection(), Then no crash."""
        from devices.bruker_2p.visualizer import plot_max_projection

        empty_stack = ImagingStack(
            frames=[],
            pixels_per_line=64,
            lines_per_frame=64,
        )
        result = plot_max_projection(empty_stack, output_path=None)
        assert isinstance(result, bytes)
