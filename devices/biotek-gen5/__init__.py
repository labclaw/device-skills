"""BioTek Gen5 device skill — microplate reader."""

from __future__ import annotations

# Guard against pytest importing this __init__.py directly without a package context.
# When imported normally (via 'devices.biotek_gen5'), relative imports work fine.
# When pytest scans the directory with a hyphenated path, __package__ may be None.
if __package__:
    from .adapter import Gen5Adapter
    from .brain import Gen5Brain
    from .processor import Gen5Processor

    __all__ = ["Gen5Adapter", "Gen5Brain", "Gen5Processor"]
else:
    # Deferred import — package will be set up via conftest before tests run
    __all__ = []
