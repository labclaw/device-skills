"""Cloud Brain for two-photon imaging — uses Claude to interpret calcium data.

Implements BaseBrain (analyze, summarize) with cached demo fallback
for offline mode when no API key is available.
"""
from __future__ import annotations

import logging
import os
from typing import Any

from device_skills.base import BaseBrain

from .processor import ROI, ImagingStack, TwoPhotonProcessor

logger = logging.getLogger(__name__)

TWO_PHOTON_SYSTEM_PROMPT = (
    "You are an expert two-photon microscopist and neuroscientist working as part of"
    " an AI scientist system called Device-Use.\n"
    "\n"
    "You receive two-photon calcium imaging data (stack metadata, ROI traces,"
    " max projections) and must:\n"
    "1. Assess image quality (SNR, motion artifacts, photobleaching)\n"
    "2. Identify cell types and layers based on morphology and depth\n"
    "3. Characterize activity patterns (transient frequency, amplitude, synchrony)\n"
    "4. Evaluate indicator expression (brightness, baseline fluorescence)\n"
    "5. Suggest imaging parameter adjustments if needed\n"
    "\n"
    "Important guidelines:\n"
    "- Be specific about imaging parameters (laser power, PMT gain, zoom, dwell time)\n"
    "- Use standard neuroscience and microscopy terminology\n"
    "- When uncertain, clearly state your confidence level\n"
    "- Consider photobleaching and phototoxicity risks\n"
    "- Always suggest at least one follow-up step (adjust power, change zoom, add Z planes)\n"
    "- For GCaMP imaging, 920 nm excitation at 20-60 mW is typical\n"
    "- For tdTomato, 1040 nm excitation is optimal\n"
    "\n"
    "Format your response as:\n"
    "## Image Quality Assessment\n"
    "[SNR, motion, bleaching evaluation]\n"
    "\n"
    "## Cell Detection\n"
    "[Number, types, layer identification]\n"
    "\n"
    "## Activity Analysis\n"
    "[Transient patterns, synchrony, notable events]\n"
    "\n"
    "## Confidence\n"
    "[High/Medium/Low with explanation]\n"
    "\n"
    "## Recommended Next Steps\n"
    "[Specific parameter adjustments or follow-up experiments]\n"
)

# Pre-cached demo responses for offline mode
_DEMO_CACHE: dict[str, dict[str, str]] = {
    "analyze": {
        "default": (
            "## Image Quality Assessment\n"
            "The imaging stack shows good signal-to-noise ratio (SNR ~8:1) with"
            " clear cellular resolution. No significant motion artifacts detected."
            " Minimal photobleaching observed across the time series (<5% baseline"
            " decrease over 1000 frames).\n"
            "\n"
            "## Cell Detection\n"
            "Approximately 45-60 putative neurons identified in the field of view"
            " based on GCaMP6f fluorescence. Cell bodies are 10-15 um in diameter,"
            " consistent with layer 2/3 cortical neurons. Neuropil signal is"
            " moderate, suggesting good indicator expression.\n"
            "\n"
            "## Activity Analysis\n"
            "Active neurons show calcium transients with typical GCaMP6f kinetics"
            " (rise time ~50 ms, decay tau ~400 ms). Approximately 30% of detected"
            " cells show spontaneous activity. No highly synchronous population"
            " events detected in this epoch.\n"
            "\n"
            "## Confidence\n"
            "Medium — This analysis is based on summary statistics. Full ROI"
            " segmentation and neuropil subtraction would increase confidence.\n"
            "\n"
            "## Recommended Next Steps\n"
            "1. Run Suite2p or CaImAn for automated ROI detection and signal extraction\n"
            "2. Apply neuropil subtraction (r = 0.7) before computing DF/F\n"
            "3. Consider acquiring a Z-stack to confirm cortical layer\n"
            "4. If longitudinal tracking is needed, acquire a reference"
            " vasculature image at 800 nm\n"
        ),
    },
    "suggest_params": {
        "gcamp": (
            "## Recommended Imaging Parameters for GCaMP\n"
            "\n"
            "**Excitation:** 920 nm (optimal two-photon cross-section for GCaMP6f/s)\n"
            "**Laser power:** Start at 20 mW at sample, increase to 40-60 mW if needed\n"
            "  - Monitor for photobleaching: >10% baseline drop in 10 min = too much power\n"
            "**PMT gain:** 600-800 V (maximize without saturating brightest cells)\n"
            "**Scan mode:** Resonant galvo at 30 Hz for calcium dynamics\n"
            "**Zoom:** 1.5-2x for single-cell resolution (0.5-1.0 um/pixel)\n"
            "**Z position:** 150-300 um below surface for layer 2/3\n"
            "**Frame averaging:** None for time-series (temporal resolution matters)\n"
            "  - Use 4-8x averaging for structural reference images only\n"
        ),
        "default": (
            "## General Imaging Parameter Suggestions\n"
            "\n"
            "Without knowing the specific indicator, here are safe starting parameters:\n"
            "**Excitation:** 920 nm (good for most GFP-based indicators)\n"
            "**Laser power:** 20-30 mW at sample (conservative start)\n"
            "**PMT gain:** 600-700 V\n"
            "**Scan mode:** Resonant galvo at 30 Hz\n"
            "**Zoom:** 1x for survey, 2x for single-cell imaging\n"
        ),
    },
    "compare": {
        "default": (
            "## Session Comparison\n"
            "\n"
            "Field of view alignment appears adequate based on metadata comparison."
            " For accurate cross-session registration:\n"
            "1. Use vasculature landmarks visible in both sessions\n"
            "2. Apply rigid translation + rotation correction\n"
            "3. Verify cell identity by matching spatial footprints\n"
            "4. Compare baseline fluorescence to detect indicator changes\n"
        ),
    },
}


def _has_api_key() -> bool:
    """Return True if an Anthropic API key is available."""
    return bool(os.environ.get("ANTHROPIC_API_KEY"))


class TwoPhotonBrain(BaseBrain):
    """Cloud Brain for two-photon imaging interpretation — wraps Claude API.

    When ``ANTHROPIC_API_KEY`` is set, calls go to the live Claude API.
    When the key is **not** set, the brain falls back to pre-cached demo
    responses. If neither is available, a ``RuntimeError`` is raised.

    Implements BaseBrain:
      analyze(data, context)   -> str
      summarize(findings)      -> str

    Additional two-photon-specific methods:
      interpret_activity(stack, rois)
      suggest_imaging_params(context)
      compare_sessions(session1, session2)
    """

    def __init__(self, model: str = "claude-sonnet-4-20250514") -> None:
        self._use_api = _has_api_key()
        if self._use_api:
            from anthropic import Anthropic

            self.client = Anthropic()
        else:
            self.client = None  # type: ignore[assignment]
            logger.info(
                "ANTHROPIC_API_KEY not set — 2P Brain will use cached demo responses"
            )
        self.model = model
        self._processor = TwoPhotonProcessor()

    # ------------------------------------------------------------------
    # BaseBrain interface
    # ------------------------------------------------------------------

    def analyze(self, data: dict[str, Any], context: str = "") -> str:
        """Analyze two-photon imaging data and return interpretation.

        Args:
            data: dict with a "stack" key (ImagingStack) or a "summary" key (str).
            context: Optional additional context string.
        """
        stack: ImagingStack | None = data.get("stack")
        if stack is not None:
            summary = self._processor.get_stack_summary(stack)
        else:
            summary = data.get("summary", str(data))

        if context:
            summary += f"\n\nAdditional context: {context}"

        if not self._use_api:
            return _DEMO_CACHE["analyze"]["default"]

        return self._call(
            TWO_PHOTON_SYSTEM_PROMPT,
            f"Please analyze this two-photon imaging data:\n\n{summary}",
        )

    def summarize(self, findings: list[str]) -> str:
        """Summarize multiple imaging analysis findings.

        Args:
            findings: List of analysis result strings.

        Returns:
            Combined summary string.
        """
        if not findings:
            return "No findings to summarize."

        combined = "\n\n---\n\n".join(findings)

        if not self._use_api:
            return f"Summary of {len(findings)} imaging findings:\n\n" + combined

        return self._call(
            TWO_PHOTON_SYSTEM_PROMPT,
            f"Summarize the following imaging findings:\n\n{combined}",
            max_tokens=1000,
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _call(self, system: str, user_message: str, max_tokens: int = 2000) -> str:
        """Non-streaming API call."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user_message}],
        )
        return response.content[0].text

    # ------------------------------------------------------------------
    # Two-photon specific public API
    # ------------------------------------------------------------------

    def interpret_activity(
        self,
        stack: ImagingStack,
        rois: list[ROI] | None = None,
        context: str = "",
    ) -> str:
        """Interpret calcium activity patterns from imaging data.

        Args:
            stack: ImagingStack with time-series frames.
            rois: Optional list of ROIs with fluorescence traces.
            context: Additional context (e.g., brain region, indicator).

        Returns:
            Analysis string.
        """
        summary = self._processor.get_stack_summary(stack)

        if rois:
            active_count = sum(1 for r in rois if r.trace is not None)
            summary += f"\n\nROIs detected: {len(rois)}"
            summary += f"\nROIs with traces: {active_count}"

        if context:
            summary += f"\n\nContext: {context}"

        if not self._use_api:
            return _DEMO_CACHE["analyze"]["default"]

        return self._call(
            TWO_PHOTON_SYSTEM_PROMPT,
            f"Interpret the calcium activity in this data:\n\n{summary}",
        )

    def suggest_imaging_params(self, context: str = "") -> str:
        """Suggest optimal imaging parameters.

        Args:
            context: What indicator/brain region/experiment type.

        Returns:
            Parameter recommendation string.
        """
        if not self._use_api:
            if "gcamp" in context.lower():
                return _DEMO_CACHE["suggest_params"]["gcamp"]
            return _DEMO_CACHE["suggest_params"]["default"]

        prompt = "Suggest optimal two-photon imaging parameters"
        if context:
            prompt += f" for: {context}"
        prompt += (
            "\n\nInclude: excitation wavelength, laser power, PMT gain,"
            " scan mode, zoom, frame rate, and Z position."
        )

        return self._call(TWO_PHOTON_SYSTEM_PROMPT, prompt, max_tokens=1500)

    def compare_sessions(
        self,
        session1: dict[str, Any],
        session2: dict[str, Any],
        context: str = "",
    ) -> str:
        """Compare two imaging sessions for FOV re-registration.

        Args:
            session1: First session metadata dict.
            session2: Second session metadata dict.
            context: Additional context.

        Returns:
            Comparison and registration guidance.
        """
        if not self._use_api:
            return _DEMO_CACHE["compare"]["default"]

        msg = (
            f"Compare these two imaging sessions for FOV registration:\n\n"
            f"--- Session 1 ---\n{session1}\n\n"
            f"--- Session 2 ---\n{session2}"
        )
        if context:
            msg += f"\n\nContext: {context}"

        return self._call(TWO_PHOTON_SYSTEM_PROMPT, msg)
