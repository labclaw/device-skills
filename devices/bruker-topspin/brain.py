"""Cloud Brain for NMR — uses Claude to interpret spectra and suggest experiments.

Implements BaseBrain (analyze, summarize) while preserving the full
Claude API integration and cached demo fallback from the original module.
"""
from __future__ import annotations

import logging
import os
import time
from collections.abc import Generator
from typing import Any

from device_skills.base import BaseBrain

from .demo_cache import find_cached_response
from .processor import NMRSpectrum, TopSpinProcessor

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Streaming simulation parameters (used when serving cached responses)
# ---------------------------------------------------------------------------
_STREAM_CHUNK_SIZE = 30  # characters per yielded chunk
_STREAM_DELAY_S = 0.05   # seconds between chunks (50 ms)


NMR_SYSTEM_PROMPT = (
    "You are an expert NMR spectroscopist and analytical chemist working as part of"
    " an AI scientist system called Device-Use.\n"
    "\n"
    "You receive processed NMR data (peak lists with chemical shifts and relative"
    " intensities) and must:\n"
    "1. Analyze the peak pattern (chemical shifts, relative intensities, splitting"
    " patterns if available)\n"
    "2. Identify functional groups present\n"
    "3. Propose candidate structures (provide IUPAC name and common name)\n"
    "4. Assess confidence in your identification\n"
    "5. Suggest next experiments to confirm the structure\n"
    "\n"
    "Important guidelines:\n"
    '- Be specific about chemical shift assignments (e.g., "δ 7.2-7.4 indicates'
    ' aromatic protons")\n'
    "- Use standard NMR terminology\n"
    "- When uncertain, clearly state your confidence level\n"
    "- Always suggest at least one follow-up experiment (13C, COSY, HSQC, HMBC, etc.)\n"
    "- If a molecular formula is provided, use it to constrain your analysis\n"
    "- Consider the solvent when interpreting chemical shifts\n"
    "\n"
    "Format your response as:\n"
    "## Peak Analysis\n"
    "[Detailed peak-by-peak analysis]\n"
    "\n"
    "## Proposed Structure\n"
    "[Most likely structure with reasoning]\n"
    "\n"
    "## Confidence\n"
    "[High/Medium/Low with explanation]\n"
    "\n"
    "## Recommended Next Steps\n"
    "[Specific experiments to run next and why]\n"
)


def _has_api_key() -> bool:
    """Return True if an Anthropic API key is available."""
    return bool(os.environ.get("ANTHROPIC_API_KEY"))


def _simulate_stream(text: str) -> Generator[str]:
    """Yield *text* in small chunks with a short delay to mimic real Claude streaming."""
    for i in range(0, len(text), _STREAM_CHUNK_SIZE):
        chunk = text[i : i + _STREAM_CHUNK_SIZE]
        time.sleep(_STREAM_DELAY_S)
        yield chunk


def _resolve_compound_name(spectrum: NMRSpectrum) -> str:
    """Extract a best-effort compound name from spectrum metadata."""
    for candidate in (spectrum.title, spectrum.sample_name):
        if candidate and candidate.strip():
            return candidate.strip()
    return ""


class TopSpinBrain(BaseBrain):
    """Cloud Brain for NMR interpretation — wraps Claude API.

    When ``ANTHROPIC_API_KEY`` is set, all calls go to the live Claude API.
    When the key is **not** set, the brain falls back to pre-cached demo
    responses (see ``demo_cache.py``). If neither an API key nor a cache
    hit is available, a clear ``RuntimeError`` is raised.

    Implements BaseBrain:
      analyze(data, context)   -> str
      summarize(findings)      -> str

    Additional NMR-specific methods:
      interpret_spectrum(spectrum, ...)
      suggest_next_experiment(spectrum, ...)
      compare_spectra(spectrum1, spectrum2, ...)
    """

    def __init__(self, model: str = "claude-sonnet-4-20250514") -> None:
        self._use_api = _has_api_key()
        if self._use_api:
            from anthropic import Anthropic

            self.client = Anthropic()
        else:
            self.client = None  # type: ignore[assignment]
            logger.info(
                "ANTHROPIC_API_KEY not set — NMR Brain will use cached demo responses"
            )
        self.model = model
        self._processor = TopSpinProcessor()

    # ------------------------------------------------------------------
    # BaseBrain interface
    # ------------------------------------------------------------------

    def analyze(self, data: dict[str, Any], context: str = "") -> str:
        """Analyze NMR data dict and return interpretation.

        Args:
            data: dict with a "spectrum" key (NMRSpectrum) or a "summary" key (str).
            context: Optional additional context string.
        """
        spectrum: NMRSpectrum | None = data.get("spectrum")
        if spectrum is not None:
            result = self.interpret_spectrum(spectrum, context=context, stream=False)
            return result if isinstance(result, str) else "".join(result)

        summary = data.get("summary", "")
        if not summary:
            summary = str(data)

        if not self._use_api:
            raise RuntimeError(
                "No ANTHROPIC_API_KEY set and no NMRSpectrum provided for cache lookup. "
                "Set ANTHROPIC_API_KEY or pass a spectrum object."
            )
        return self._call(NMR_SYSTEM_PROMPT, f"Please analyze this NMR data:\n\n{summary}")

    def summarize(self, findings: list[str]) -> str:
        """Summarize multiple NMR findings into a coherent narrative."""
        if not findings:
            return "No findings to summarize."

        combined = "\n\n---\n\n".join(findings)
        prompt = (
            f"Summarize the following NMR analysis findings into a concise narrative:\n\n"
            f"{combined}"
        )

        if not self._use_api:
            # Return a simple concatenation in offline mode
            return f"Summary of {len(findings)} NMR findings:\n\n" + combined

        return self._call(NMR_SYSTEM_PROMPT, prompt, max_tokens=1000)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _build_summary(self, spectrum: NMRSpectrum) -> str:
        return self._processor.get_spectrum_summary(spectrum)

    def _call(self, system: str, user_message: str, max_tokens: int = 2000) -> str:
        """Non-streaming API call."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user_message}],
        )
        return response.content[0].text

    def _stream(
        self, system: str, user_message: str, max_tokens: int = 2000
    ) -> Generator[str]:
        """Streaming API call — yields text chunks."""
        with self.client.messages.stream(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user_message}],
        ) as stream:
            yield from stream.text_stream

    def _cached_or_error(
        self,
        spectrum: NMRSpectrum,
        response_type: str,
        stream: bool,
    ) -> str | Generator[str]:
        """Try to serve a cached demo response; raise if nothing is available."""
        compound = _resolve_compound_name(spectrum)
        cached = find_cached_response(compound, response_type) if compound else None

        if cached is None:
            raise RuntimeError(
                f"No ANTHROPIC_API_KEY set and no cached demo response found "
                f"for compound '{compound or '<unknown>'}'. "
                f"Set the ANTHROPIC_API_KEY environment variable to enable "
                f"live Claude analysis, or use one of the built-in demo "
                f"compounds (alpha ionone, strychnine)."
            )

        logger.info("Serving cached %s response for '%s'", response_type, compound)
        if stream:
            return _simulate_stream(cached)
        return cached

    # ------------------------------------------------------------------
    # NMR-specific public API
    # ------------------------------------------------------------------

    def interpret_spectrum(
        self,
        spectrum: NMRSpectrum,
        molecular_formula: str | None = None,
        context: str = "",
        stream: bool = False,
    ) -> str | Generator[str]:
        """Send spectrum data to Claude for interpretation."""
        if not self._use_api:
            return self._cached_or_error(spectrum, "interpret", stream)

        summary = self._build_summary(spectrum)

        user_message = f"Please analyze this NMR spectrum:\n\n{summary}"
        if molecular_formula:
            user_message += f"\n\nMolecular formula: {molecular_formula}"
        if context:
            user_message += f"\n\nAdditional context: {context}"

        if stream:
            return self._stream(NMR_SYSTEM_PROMPT, user_message)
        return self._call(NMR_SYSTEM_PROMPT, user_message)

    def suggest_next_experiment(
        self,
        spectrum: NMRSpectrum,
        hypothesis: str = "",
        stream: bool = False,
    ) -> str | Generator[str]:
        """Given current data, suggest the most informative next experiment."""
        if not self._use_api:
            return self._cached_or_error(spectrum, "suggest_next_experiment", stream)

        summary = self._build_summary(spectrum)

        user_message = (
            f"Based on this NMR data, what experiment should I run next?\n\n"
            f"{summary}"
        )
        if hypothesis:
            user_message += f"\n\nCurrent hypothesis: {hypothesis}"
        user_message += (
            "\n\nProvide a specific recommendation with:\n"
            "1. Which experiment (COSY, HSQC, HMBC, 13C, DEPT, NOESY, etc.)\n"
            "2. Why this experiment is most informative right now\n"
            "3. What specific question it will answer\n"
            "4. Expected key correlations to look for"
        )

        if stream:
            return self._stream(NMR_SYSTEM_PROMPT, user_message, max_tokens=1500)
        return self._call(NMR_SYSTEM_PROMPT, user_message, max_tokens=1500)

    def compare_spectra(
        self,
        spectrum1: NMRSpectrum,
        spectrum2: NMRSpectrum,
        context: str = "",
    ) -> str:
        """Compare two NMR spectra — for purity/batch comparison."""
        if not self._use_api:
            raise RuntimeError(
                "No ANTHROPIC_API_KEY set. Spectrum comparison is not available "
                "in demo mode. Set the ANTHROPIC_API_KEY environment variable "
                "to enable live Claude analysis."
            )

        summary1 = self._build_summary(spectrum1)
        summary2 = self._build_summary(spectrum2)

        user_message = (
            f"Compare these two NMR spectra and identify any differences:\n\n"
            f"--- Spectrum 1 ---\n{summary1}\n\n"
            f"--- Spectrum 2 ---\n{summary2}"
        )
        if context:
            user_message += f"\n\nContext: {context}"

        return self._call(NMR_SYSTEM_PROMPT, user_message)


# Backward-compatible alias
NMRBrain = TopSpinBrain
