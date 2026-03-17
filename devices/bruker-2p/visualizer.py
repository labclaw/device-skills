"""Two-photon imaging visualization — max projections, FOV overlays, calcium traces."""

from __future__ import annotations

import io
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from .processor import ROI, ImagingStack


def plot_max_projection(
    stack: ImagingStack,
    output_path: str | Path | None = "max_projection.png",
    title: str | None = None,
    show_scale_bar: bool = True,
    channel: int = 1,
) -> Path | bytes:
    """Plot max intensity projection with scale bar and metadata.

    Args:
        stack: ImagingStack to project.
        output_path: File path to save, or None to return PNG bytes.
        title: Override plot title.
        show_scale_bar: Whether to draw a scale bar.
        channel: Channel number to project.

    Returns:
        Path to saved image if output_path is given, or raw PNG bytes.
    """
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from .processor import TwoPhotonProcessor

    proc = TwoPhotonProcessor()
    max_proj = proc.max_projection(stack, channel=channel)

    return_bytes = output_path is None
    if not return_bytes:
        output_path = Path(output_path)

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    ax.imshow(max_proj, cmap="gray", aspect="equal")
    ax.set_axis_off()

    # Scale bar
    if show_scale_bar and stack.microns_per_pixel_x > 0:
        bar_um = 50  # 50 um scale bar
        bar_px = bar_um / stack.microns_per_pixel_x
        y_pos = max_proj.shape[0] * 0.95
        x_start = max_proj.shape[1] * 0.05
        ax.plot(
            [x_start, x_start + bar_px],
            [y_pos, y_pos],
            color="white",
            linewidth=3,
        )
        ax.text(
            x_start + bar_px / 2,
            y_pos - max_proj.shape[0] * 0.02,
            f"{bar_um} um",
            color="white",
            fontsize=10,
            ha="center",
            fontweight="bold",
        )

    # Title
    plot_title = title or _build_projection_title(stack)
    ax.set_title(plot_title, fontsize=14, fontweight="bold", pad=10, color="white")

    # Metadata subtitle
    subtitle_parts = []
    if stack.laser_wavelength > 0:
        subtitle_parts.append(f"{stack.laser_wavelength:.0f} nm")
    if stack.laser_power > 0:
        subtitle_parts.append(f"{stack.laser_power:.0f} mW")
    if stack.scan_mode:
        subtitle_parts.append(stack.scan_mode)
    if subtitle_parts:
        ax.text(
            0.5,
            1.01,
            " | ".join(subtitle_parts),
            transform=ax.transAxes,
            ha="center",
            fontsize=10,
            color="#666666",
        )

    # Branding
    ax.text(
        0.99,
        0.01,
        "Bruker 2P | device-skills",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=8,
        color="#999999",
        style="italic",
    )

    fig.patch.set_facecolor("black")
    plt.tight_layout()

    if return_bytes:
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=200, bbox_inches="tight", facecolor="black")
        plt.close(fig)
        buf.seek(0)
        return buf.read()
    else:
        fig.savefig(str(output_path), dpi=200, bbox_inches="tight", facecolor="black")
        plt.close(fig)
        return output_path


def plot_fov_overlay(
    reference: np.ndarray,
    current: np.ndarray,
    output_path: str | Path | None = "fov_overlay.png",
    title: str | None = None,
) -> Path | bytes:
    """Overlay two FOV images for registration comparison.

    Reference is shown in magenta, current in green. Aligned regions
    appear white.

    Args:
        reference: 2D array — reference session image.
        current: 2D array — current session image.
        output_path: File path to save, or None to return PNG bytes.
        title: Override plot title.

    Returns:
        Path to saved image if output_path is given, or raw PNG bytes.
    """
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    return_bytes = output_path is None
    if not return_bytes:
        output_path = Path(output_path)

    # Normalize both images to [0, 1]
    ref_norm = _normalize_image(reference)
    cur_norm = _normalize_image(current)

    # Ensure same shape (crop to smaller)
    min_h = min(ref_norm.shape[0], cur_norm.shape[0])
    min_w = min(ref_norm.shape[1], cur_norm.shape[1])
    ref_norm = ref_norm[:min_h, :min_w]
    cur_norm = cur_norm[:min_h, :min_w]

    # RGB composite: reference=magenta, current=green
    composite = np.zeros((*ref_norm.shape, 3))
    composite[:, :, 0] = ref_norm  # Red from reference
    composite[:, :, 1] = cur_norm  # Green from current
    composite[:, :, 2] = ref_norm  # Blue from reference (magenta = R+B)

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.imshow(composite, aspect="equal")
    ax.set_axis_off()

    plot_title = title or "FOV Overlay — Magenta: Reference | Green: Current"
    ax.set_title(plot_title, fontsize=12, fontweight="bold", pad=10)

    fig.patch.set_facecolor("black")
    plt.tight_layout()

    if return_bytes:
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=200, bbox_inches="tight", facecolor="black")
        plt.close(fig)
        buf.seek(0)
        return buf.read()
    else:
        fig.savefig(str(output_path), dpi=200, bbox_inches="tight", facecolor="black")
        plt.close(fig)
        return output_path


def plot_calcium_traces(
    rois: list[ROI],
    frame_rate: float,
    output_path: str | Path | None = "calcium_traces.png",
    title: str | None = None,
    max_rois: int = 10,
) -> Path | bytes:
    """Plot fluorescence traces (DF/F) for detected ROIs.

    Args:
        rois: List of ROI objects with fluorescence traces.
        frame_rate: Frame rate in Hz for time axis.
        output_path: File path to save, or None to return PNG bytes.
        title: Override plot title.
        max_rois: Maximum number of ROIs to display.

    Returns:
        Path to saved image if output_path is given, or raw PNG bytes.
    """
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    return_bytes = output_path is None
    if not return_bytes:
        output_path = Path(output_path)

    # Filter to ROIs with traces
    rois_with_traces = [r for r in rois if r.trace is not None and len(r.trace) > 0]
    rois_to_plot = rois_with_traces[:max_rois]

    n_rois = len(rois_to_plot)
    if n_rois == 0:
        # Empty plot
        fig, ax = plt.subplots(1, 1, figsize=(12, 4))
        ax.text(
            0.5,
            0.5,
            "No ROI traces to display",
            ha="center",
            va="center",
            fontsize=14,
            color="#666666",
            transform=ax.transAxes,
        )
        ax.set_axis_off()
    else:
        fig, axes = plt.subplots(n_rois, 1, figsize=(12, 2 * n_rois), sharex=True)
        if n_rois == 1:
            axes = [axes]

        for i, roi in enumerate(rois_to_plot):
            ax = axes[i]
            trace = roi.trace

            # Compute DF/F
            baseline = np.percentile(trace, 10)
            if baseline > 0:
                df_f = (trace - baseline) / baseline
            else:
                df_f = trace

            # Time axis
            if frame_rate > 0:
                time_s = np.arange(len(df_f)) / frame_rate
                ax.plot(time_s, df_f, color="#2ecc71", linewidth=0.8)
                ax.set_xlabel("Time (s)")
            else:
                ax.plot(df_f, color="#2ecc71", linewidth=0.8)
                ax.set_xlabel("Frame")

            ax.set_ylabel(f"ROI {roi.id}\nDF/F", fontsize=9)
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)

    plot_title = title or "Calcium Traces (DF/F)"
    fig.suptitle(plot_title, fontsize=14, fontweight="bold")
    plt.tight_layout()

    if return_bytes:
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=200, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        buf.seek(0)
        return buf.read()
    else:
        fig.savefig(str(output_path), dpi=200, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        return output_path


def _normalize_image(img: np.ndarray) -> np.ndarray:
    """Normalize an image to [0, 1] float range."""
    img = img.astype(np.float64)
    vmin, vmax = img.min(), img.max()
    if vmax > vmin:
        return (img - vmin) / (vmax - vmin)
    return np.zeros_like(img)


def _build_projection_title(stack: ImagingStack) -> str:
    """Build a title from stack metadata."""
    parts = ["Max Intensity Projection"]
    if stack.objective:
        parts.append(stack.objective)
    parts.append(f"{len(stack.frames)} frames")
    return " — ".join(parts)
