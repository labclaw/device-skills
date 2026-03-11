"""Bruker TopSpin NMR device skill.

Three control modes, one consistent output:
  - API mode: gRPC to running TopSpin (port 3081)
  - GUI mode: Computer Use visual automation
  - Offline mode: nmrglue processing without TopSpin

Public API::

    from devices.bruker_topspin import TopSpinAdapter, TopSpinBrain, TopSpinProcessor
    from devices.bruker_topspin import NMRSpectrum, NMRPeak

    adapter = TopSpinAdapter()          # defaults to OFFLINE mode
    adapter.connect()
    spectrum = adapter.process("/opt/topspin5.0.0/examdata/exam_CMCse_1/1")

    brain = TopSpinBrain()
    interpretation = brain.interpret_spectrum(spectrum)
"""
from __future__ import annotations

# Guard against pytest importing this __init__.py directly without a package context.
# When imported normally (via 'devices.bruker_topspin'), relative imports work fine.
# When pytest scans the directory with a hyphenated path, __package__ may be None.
if __package__:
    from .adapter import TopSpinAdapter
    from .brain import TopSpinBrain
    from .processor import NMRPeak, NMRSpectrum, TopSpinProcessor

    __all__ = [
        "TopSpinAdapter",
        "TopSpinBrain",
        "TopSpinProcessor",
        "NMRSpectrum",
        "NMRPeak",
    ]
else:
    __all__ = []
