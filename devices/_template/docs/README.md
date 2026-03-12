# Documentation — [Device Name]

Place official vendor documentation in this directory, organized by subdirectory:

- `manual/` — Operator manuals, safety manuals, quick-start guides
- `api/` — Programming interface references (COM, REST, gRPC, serial protocols)
- `specs/` — Hardware specifications, datasheets, component details
- `formats/` — Data file format documentation (schemas, naming conventions, parsing guides)
- `science/` — Domain science background relevant to this instrument

## Guidelines

- Use Markdown files (`.md`) for all documentation.
- Summarize vendor PDFs into structured Markdown — do not commit large binary files.
- Cite sources: include page numbers, section references, or URLs.
- Mark any community-inferred or unverified information with `[UNVERIFIED]`.
- Keep files focused: one topic per file (e.g., `safety_manual.md`, `laser_specs.md`).
- An AI agent should be able to read these files and fully understand the device.
