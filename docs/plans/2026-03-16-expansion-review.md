# Device-Skills EXPANSION Review — 2026-03-16

## Review Mode: SCOPE EXPANSION
## Status: Complete — auto-approved recommended options

---

## Executive Summary

Device-skills is the **knowledge layer** of the LabClaw ecosystem — the shared vocabulary that both device-use (hands) and labclaw (brain) consume. At v0.1.0 with 146 tests, 3 device implementations + 1 template, and excellent documentation, it's the **most mature** subproject. However, it lacks coverage enforcement, cross-repo integration tests, and consistent BDD formatting.

**Grade: B+ (Pre-Production).** Foundation is solid enough to start Micro-Manager expansion. Complete P0 governance fixes first (~12 hours).

---

## System Audit

| Metric | Value |
|--------|-------|
| Version | v0.1.0, Python 3.11+ |
| Source | `src/device_skills/` (base abstractions) + `devices/` (3 + template) |
| Tests | 146 total, 1,778 lines test code |
| Coverage | **Not enforced** (no `fail_under`) ★ |
| BDD | Partial — docstring-based, inconsistent across devices ★ |
| Dependencies | Minimal: pydantic, pyyaml; optional per-device extras |
| CI | pytest + ruff + mypy, all passing |
| Documentation | Excellent: CLAUDE.md, ROADMAP, skill.yaml template, SOUL.md per device |

## Architecture

```
device-skills/
├── src/device_skills/        ← Shared abstractions
│   ├── base.py               ← BaseDriver, BaseAdapter, BaseProcessor, BaseBrain
│   ├── schema.py             ← SkillManifest, ControlMode, DeviceCapabilities
│   └── loader.py             ← discover_skills(), load_manifest()
│
├── devices/
│   ├── _template/            ← Copy-to-create scaffold
│   ├── bruker-topspin/       ← NMR (API/GUI/Offline, 100+ cmd docs)
│   │   ├── docs/             ← Official RAG (immutable, 100+ files)
│   │   └── (missing user/)   ★ GAP
│   ├── bruker-2p/            ← Two-photon microscope (PrairieLink)
│   │   ├── docs/             ✅
│   │   └── user/             ✅
│   └── biotek-gen5/          ← Plate reader
│       ├── docs/             ✅ (minimal)
│       └── user/             ✅
```

### Per-Device Structure (Standard Template)

```
METADATA:   skill.yaml → SOUL.md → MEMORY.md → SKILL.md → profile.yaml
CODE:       driver.py → adapter.py → processor.py → brain.py → visualizer.py
KNOWLEDGE:  docs/ (official, immutable) + user/ (accumulated, mutable)
TESTS:      tests/test_device.py
```

**Consumed by:**
- **device-use**: imports BaseAdapter, reads skill.yaml + profile.yaml, uses SkillContext for prompts
- **labclaw**: imports BaseDriver, reads skill.yaml for hardware registry
- **labwork**: displays device metadata from skill.yaml

## Section 1: Architecture Review

**Strengths:**
- Clean ABC hierarchy (BaseDriver/Adapter/Processor/Brain) — no god classes
- Three control modes (API/GUI/Offline) consistent across all devices
- Progressive disclosure: docs/ (official RAG) vs user/ (accumulated experience)
- skill.yaml as structured manifest → consumed by both device-use and labclaw

**Issues:**
1. **bruker-topspin missing user/ directory** — two-layer RAG incomplete
2. **No cross-repo integration tests** — BaseDriver/BaseAdapter contract not verified against consumers
3. **No validation that skill.yaml matches actual implementation** — metadata can drift
4. **Hardcoded password in bruker-2p** — `password: str = "0000"` sets bad pattern

**Expansion opportunity:** As device count grows (target: 20+), need instrument-type base classes (BaseImagingDevice, BasePlateReaderDevice). Defer until 3+ similar devices exist.

## Section 2: Error & Rescue Map

| Method | Failure | Rescued? |
|--------|---------|----------|
| discover_skills() | Invalid skill.yaml | Y — logs warning, skips |
| BaseDriver.connect() | Hardware unreachable | Y — returns False |
| BaseBrain.analyze() | No API key | Y — falls back to demo cache |
| load_manifest() | Missing required fields | Y — Pydantic validation error |
| SkillContext.build_prompt() | RAG retrieval fails | Y — skips L3, continues |

**No critical gaps.** Error handling is thorough. The demo cache fallback pattern is well-implemented.

## Section 3: Security

| Threat | Severity | Mitigated? |
|--------|----------|------------|
| Hardcoded password (bruker-2p) | LOW | PARTIAL — demo context, but bad pattern |
| API keys in brain.py | — | OK ✅ — via env var, cache fallback |
| File path handling | — | OK ✅ — pathlib throughout |
| No shell injection | — | OK ✅ — no subprocess/eval/exec |

## Section 4-10: Consolidated

**Code Quality:** A — type-safe, DRY at right level, ruff + mypy passing. Only anti-pattern: brain.py caches as Python dicts (should be JSON/YAML for easier updates).

**Tests:** B+ — 146 tests, good scenarios. Missing: coverage enforcement gate, consistent BDD format, cross-repo compatibility tests.

**Performance:** Not a concern — skill loading is startup-only, O(N) where N = number of devices.

**Observability:** Missing — no structured logging, no audit trail for adapter lifecycle.

**Deployment:** Ready — hatchling build, pyproject.toml versioning, optional extras per device.

**Long-term:** Reversibility 5/5. At 20+ devices, need marketplace model (core devices in-repo, community in external repos).

---

## Failure Modes Registry

```
CODEPATH              | FAILURE          | RESCUED? | TEST? | USER SEES
──────────────────────┼──────────────────┼──────────┼───────┼──────────
discover_skills()     | Bad YAML         | Y        | Y     | Warning log
BaseDriver.connect()  | No hardware      | Y        | Y     | False return
BaseBrain.analyze()   | No API key       | Y        | Y     | Cached response
load_manifest()       | Invalid schema   | Y        | Y     | ValidationError
SkillContext RAG      | Missing docs/    | Y        | Y     | Prompt w/o L3
```

**Zero CRITICAL gaps.** Device-skills is the healthiest repo in the ecosystem.

---

## Priority Roadmap

### P0 (12 hours)
- DS1: Coverage enforcement (≥80%)
- DS2: BDD test format enforcement
- DS3: Move hardcoded password to env var
- DS4: Complete bruker-topspin user/
- DS5: Cross-repo integration tests

### P1 (7 hours)
- DS6: Skill validation layer (yaml ↔ implementation match)
- DS7: Structured logging

### P2 (50+ hours)
- DS8: Micro-Manager skill (highest ROI expansion)

---

## Key Decisions (Auto-Selected Recommended)

1. **BDD format**: Naming convention (light) for unit tests; pytest-bdd optional for integration
2. **skill.yaml**: Keep current approach for v0.2.0; extend with workflow metadata in v0.4.0+
3. **Cross-device abstraction**: Keep isolated for v0.2.0; extract base classes after 3+ similar devices
4. **Marketplace**: Core devices in-repo through v1.0; external registry after 5-6 devices shipped
