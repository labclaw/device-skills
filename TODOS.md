# TODOS.md — Device-Skills

> Generated from EXPANSION Review 2026-03-16

## P0 — Governance (before v0.2.0, ~12 hours)

### TODO-DS1: Coverage Enforcement
- **What:** Add `--cov-fail-under=80` to Makefile test target and CI workflow.
- **Why:** No automated coverage gate exists. New devices can ship with low coverage.
- **Effort:** S (1 hour)
- **Priority:** P0

### TODO-DS2: BDD Test Format Enforcement
- **What:** Adopt consistent BDD naming convention across all device tests. Enforce `test_given_<scenario>_when_<action>_then_<result>` pattern. Update _template test to demonstrate.
- **Why:** Tests are inconsistent — bruker-2p uses BDD-style docstrings, biotek-gen5 uses plain names. Project convention mandates BDD.
- **Effort:** S (2 hours)
- **Priority:** P0

### TODO-DS3: Move Hardcoded Password to Env Var
- **What:** Change bruker-2p adapter.py `password: str = "0000"` to `password: str = os.getenv("PRAIRIE_PASSWORD", "0000")`. Document why default exists.
- **Why:** Sets bad pattern for future devices. Demo fallback is fine but should be explicit.
- **Effort:** S (1 hour)
- **Priority:** P0

### TODO-DS4: Complete bruker-topspin user/ Directory
- **What:** Create `devices/bruker-topspin/user/` with MEMORY.md, system_config.md, calibration_log.md, protocols/, findings/. Mirror structure from bruker-2p and biotek-gen5.
- **Why:** Two-layer RAG (docs/ + user/) is the standard template. bruker-topspin is missing user/.
- **Effort:** S (1 hour)
- **Priority:** P0

### TODO-DS5: Cross-Repo Integration Tests
- **What:** Add `tests/test_cross_repo_compat.py` that verifies device-use can load adapters and labclaw can instantiate drivers from skill.yaml.
- **Why:** Breaking changes to BaseDriver/BaseAdapter could slip through. No automated cross-repo verification exists.
- **Effort:** M (4 hours)
- **Priority:** P0

## P1 — Production Hardening

### TODO-DS6: Skill Validation Layer
- **What:** Add `src/device_skills/validator.py` — `validate_device(device_dir)` checks skill.yaml capabilities match actual adapter implementation. Integrate into loader.
- **Why:** Metadata (skill.yaml) can drift from reality. Automated validation catches mismatches.
- **Effort:** M (3 hours)
- **Priority:** P1

### TODO-DS7: Structured Logging
- **What:** Add `logging.getLogger(__name__)` to all modules. Standardize log levels. Add audit trail for adapter lifecycle.
- **Why:** No observability for device operations. Required before production lab deployment.
- **Effort:** M (4 hours)
- **Priority:** P1

## P2 — Expansion

### TODO-DS8: Micro-Manager Skill
- **What:** Create `devices/micro-manager/` with full driver/adapter/processor/brain implementation. Simulation-first imaging skill.
- **Why:** Highest ROI expansion target per ROADMAP.md.
- **Effort:** XL (50 hours)
- **Priority:** P2
