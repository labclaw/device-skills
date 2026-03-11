"""pytest configuration for bruker-topspin tests.

Registers the bruker-topspin device package under the importable name
'devices.bruker_topspin' so that tests can use standard Python import syntax.

Python cannot import directories with hyphens, so we load each module
explicitly via importlib.util and register it in sys.modules under the
underscore-based canonical name.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_DEVICE_DIR = Path(__file__).parent.parent  # .../devices/bruker-topspin/
_REPO_ROOT = _DEVICE_DIR.parent.parent      # .../device-skills/

# Ensure src/ is on path for device_skills imports
_src = str(_REPO_ROOT / "src")
if _src not in sys.path:
    sys.path.insert(0, _src)

# Ensure the repo root is on path for the 'devices' namespace
_root = str(_REPO_ROOT)
if _root not in sys.path:
    sys.path.insert(0, _root)

_PKG_NAME = "devices.bruker_topspin"

# Establish parent namespace packages if not present
if "devices" not in sys.modules:
    import types
    _devices_ns = types.ModuleType("devices")
    _devices_ns.__path__ = [str(_REPO_ROOT / "devices")]  # type: ignore[assignment]
    _devices_ns.__package__ = "devices"
    sys.modules["devices"] = _devices_ns

if _PKG_NAME not in sys.modules:
    # Load each submodule explicitly and register under canonical underscore name.
    # Order matters: dependencies must be loaded before dependents.
    _SUBMODULES = [
        "processor",
        "demo_cache",
        "adapter",
        "brain",
        "library",
        "visualizer",
        "gui_automation",
        "driver",
    ]

    def _load(name: str) -> None:
        full_name = f"{_PKG_NAME}.{name}"
        if full_name in sys.modules:
            return
        spec = importlib.util.spec_from_file_location(
            full_name,
            str(_DEVICE_DIR / f"{name}.py"),
        )
        if spec is None or spec.loader is None:
            raise ImportError(f"Cannot find spec for {full_name}")
        mod = importlib.util.module_from_spec(spec)
        mod.__package__ = _PKG_NAME
        sys.modules[full_name] = mod
        spec.loader.exec_module(mod)  # type: ignore[union-attr]

    for _sub in _SUBMODULES:
        _load(_sub)

    # Load __init__ and register as the package itself
    _init_spec = importlib.util.spec_from_file_location(
        _PKG_NAME,
        str(_DEVICE_DIR / "__init__.py"),
        submodule_search_locations=[str(_DEVICE_DIR)],
    )
    if _init_spec and _init_spec.loader:
        _pkg_mod = importlib.util.module_from_spec(_init_spec)
        _pkg_mod.__package__ = _PKG_NAME
        _pkg_mod.__path__ = [str(_DEVICE_DIR)]  # type: ignore[assignment]
        # Register BEFORE exec_module so relative imports in __init__.py resolve
        sys.modules[_PKG_NAME] = _pkg_mod
        try:
            _init_spec.loader.exec_module(_pkg_mod)  # type: ignore[union-attr]
        except Exception:
            # Pop if exec fails to avoid a broken cached module
            sys.modules.pop(_PKG_NAME, None)
            raise
