"""Root conftest — registers hyphenated device directories as importable packages.

Python cannot import directories with hyphens (e.g. 'biotek-gen5').
This conftest scans devices/ for such directories and registers each
under its underscore-canonical name (e.g. 'devices.biotek_gen5') using
importlib so that tests can do: `from devices.biotek_gen5.adapter import ...`
"""
from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path

_REPO_ROOT = Path(__file__).parent
_DEVICES_DIR = _REPO_ROOT / "devices"

# Ensure src/ is on path for device_skills imports
_src = str(_REPO_ROOT / "src")
if _src not in sys.path:
    sys.path.insert(0, _src)

# Ensure repo root is on path
_root = str(_REPO_ROOT)
if _root not in sys.path:
    sys.path.insert(0, _root)

# Establish 'devices' namespace package
if "devices" not in sys.modules:
    _devices_ns = types.ModuleType("devices")
    _devices_ns.__path__ = [str(_DEVICES_DIR)]
    _devices_ns.__package__ = "devices"
    sys.modules["devices"] = _devices_ns


def _load_module(pkg_name: str, mod_name: str, file_path: Path) -> None:
    """Load a single .py file and register it in sys.modules."""
    full_name = f"{pkg_name}.{mod_name}"
    if full_name in sys.modules:
        return
    spec = importlib.util.spec_from_file_location(full_name, str(file_path))
    if spec is None or spec.loader is None:
        return  # skip if file doesn't exist
    mod = importlib.util.module_from_spec(spec)
    mod.__package__ = pkg_name
    sys.modules[full_name] = mod
    spec.loader.exec_module(mod)


def _register_device(device_dir: Path) -> None:
    """Register a hyphenated device directory as an importable package."""
    canonical = device_dir.name.replace("-", "_")
    pkg_name = f"devices.{canonical}"

    if pkg_name in sys.modules:
        return

    # Register package shell FIRST so relative imports resolve
    pkg_mod = types.ModuleType(pkg_name)
    pkg_mod.__path__ = [str(device_dir)]
    pkg_mod.__package__ = pkg_name
    sys.modules[pkg_name] = pkg_mod

    # Find and load all .py submodules (except __init__)
    submodules = [
        p.stem for p in sorted(device_dir.glob("*.py"))
        if p.stem != "__init__"
    ]
    for sub in submodules:
        _load_module(pkg_name, sub, device_dir / f"{sub}.py")

    # Execute __init__.py to populate the package exports
    init_file = device_dir / "__init__.py"
    if init_file.exists():
        init_spec = importlib.util.spec_from_file_location(
            pkg_name, str(init_file),
            submodule_search_locations=[str(device_dir)],
        )
        if init_spec and init_spec.loader:
            pkg_mod.__file__ = str(init_file)
            try:
                init_spec.loader.exec_module(pkg_mod)
            except Exception:
                sys.modules.pop(pkg_name, None)
                raise


# Register all hyphenated device directories
if _DEVICES_DIR.is_dir():
    for child in sorted(_DEVICES_DIR.iterdir()):
        if (
            child.is_dir()
            and not child.name.startswith("_")
            and "-" in child.name
        ):
            _register_device(child)
