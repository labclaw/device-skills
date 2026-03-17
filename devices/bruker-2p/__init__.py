"""Bruker Ultima Investigator two-photon microscope device skill.

Three control modes, one consistent output:
  - API mode: PrairieLink COM/TCP to running PrairieView
  - GUI mode: Computer Use visual automation of PrairieView
  - Offline mode: OME-TIFF + XML processing without PrairieView

Public API::

    from devices.bruker_2p import TwoPhotonAdapter, TwoPhotonBrain, TwoPhotonProcessor
    from devices.bruker_2p import ImagingStack, CalciumFrame, ROI

    adapter = TwoPhotonAdapter()          # defaults to OFFLINE mode
    adapter.connect()
    stack = adapter.process("/path/to/prairie_data")

    brain = TwoPhotonBrain()
    interpretation = brain.analyze({"stack": stack})
"""

from __future__ import annotations

# Guard against pytest importing this __init__.py directly without a package context.
# When imported normally (via 'devices.bruker_2p'), relative imports work fine.
# When pytest scans the directory with a hyphenated path, __package__ may be None.
if __package__:
    from .adapter import TwoPhotonAdapter
    from .brain import TwoPhotonBrain
    from .processor import ROI, CalciumFrame, ImagingStack, TwoPhotonProcessor

    __all__ = [
        "TwoPhotonAdapter",
        "TwoPhotonBrain",
        "TwoPhotonProcessor",
        "ImagingStack",
        "CalciumFrame",
        "ROI",
    ]
else:
    __all__ = []
