# Common Assay Protocols — BioTek Synergy H1

**Source:** Standard laboratory protocols; items marked [UNVERIFIED] need confirmation
against BioTek application notes.

## ELISA (Enzyme-Linked Immunosorbent Assay)

### Overview

Colorimetric immunoassay that uses enzyme-substrate reactions to produce a measurable
absorbance signal proportional to analyte concentration.

### Typical Settings

| Parameter | Value |
|-----------|-------|
| Read mode | Absorbance, endpoint |
| Wavelength | 450 nm (HRP/TMB substrate) |
| Reference wavelength | 540 nm or 570 nm (optional correction) |
| Plate format | 96-well flat-bottom |
| Shaking | 5 sec linear shake before read |
| Temperature | Room temperature (20-25C) or 37C |

### Plate Layout Convention

- **Columns 1-2:** Standards (serial dilution, highest concentration in row A)
- **Columns 3-10:** Samples (duplicates or triplicates)
- **Columns 11-12:** Blanks (substrate only, no analyte)

### Data Analysis

1. Subtract blank average from all wells.
2. Plot standard curve: OD vs. known concentration.
3. Fit curve (4-parameter logistic recommended for ELISA).
4. Interpolate sample concentrations from the curve.

### Quality Control

- Blank OD should be < 0.1 (ideally < 0.05).
- Standard curve R-squared should be > 0.99.
- Duplicate CV% should be < 15%.

---

## Cell Viability — MTT / XTT / MTS Assays

### Overview

Colorimetric assays measuring mitochondrial metabolic activity as a proxy for cell
viability. Living cells reduce tetrazolium salts to colored formazan products.

### Typical Settings

| Parameter | Value |
|-----------|-------|
| Read mode | Absorbance, endpoint |
| Wavelength | 570 nm (MTT), 490 nm (MTS/XTT) |
| Reference wavelength | 650 nm (background correction) |
| Plate format | 96-well flat-bottom |
| Temperature | Room temperature |

### Notes

- MTT requires solubilization step (DMSO) before reading. MTS/XTT are soluble and
  read directly.
- Allow 1-4 hours incubation with reagent before reading (assay-dependent).

---

## Cell Viability — Fluorescence (Calcein AM, Resazurin)

### Overview

Fluorescence-based viability assays. Calcein AM is cleaved by intracellular esterases
in live cells to produce fluorescent calcein. Resazurin (alamarBlue) is reduced to
fluorescent resorufin by metabolically active cells.

### Typical Settings — Calcein AM

| Parameter | Value |
|-----------|-------|
| Read mode | Fluorescence, endpoint, bottom read |
| Excitation | 485 nm |
| Emission | 530 nm |
| Optics position | Bottom |
| Gain | 50 (auto-gain recommended) |
| Plate format | 96-well black, clear bottom |

### Typical Settings — Resazurin / alamarBlue

| Parameter | Value |
|-----------|-------|
| Read mode | Fluorescence, endpoint |
| Excitation | 530-560 nm |
| Emission | 590 nm |
| Optics position | Top or bottom |
| Gain | Auto |

---

## Protein Quantification — Bradford Assay

### Overview

Coomassie Brilliant Blue G-250 dye binds protein, shifting absorbance from 465 nm
(brown) to 595 nm (blue). Quick, inexpensive protein quantification.

### Typical Settings

| Parameter | Value |
|-----------|-------|
| Read mode | Absorbance, endpoint |
| Wavelength | 595 nm |
| Plate format | 96-well flat-bottom |
| Shaking | 5 sec before read |
| Standard | BSA (bovine serum albumin), 0-2 mg/mL |

### Notes

- Incubate 5-10 minutes at RT after adding reagent, read within 60 minutes.
- Linear range: approximately 0.1-1.0 mg/mL (standard assay). [UNVERIFIED]
- Micro assay: 1-25 ug/mL range. [UNVERIFIED]

---

## Protein Quantification — BCA Assay

### Overview

Bicinchoninic acid assay. Protein reduces Cu2+ to Cu1+; BCA chelates Cu1+ to form a
purple complex absorbing at 562 nm. More tolerant of detergents than Bradford.

### Typical Settings

| Parameter | Value |
|-----------|-------|
| Read mode | Absorbance, endpoint |
| Wavelength | 562 nm |
| Plate format | 96-well flat-bottom |
| Temperature | 37C incubation for 30 min |
| Standard | BSA, 0-2 mg/mL (working range) |

---

## Nucleic Acid Quantification

### Overview

Direct UV absorbance measurement of DNA, RNA, or oligonucleotides. Uses the 260 nm
absorption peak of nucleic acids.

### Typical Settings

| Parameter | Value |
|-----------|-------|
| Read mode | Absorbance, endpoint |
| Wavelength | 260 nm |
| Reference wavelength | 280 nm (A260/A280 purity ratio) |
| Secondary reference | 230 nm (A260/A230 purity ratio) [UNVERIFIED] |
| Plate format | UV-transparent 96-well plate (e.g., Corning UV plate) |

### Quality Metrics

- **A260/A280:** Pure DNA ~1.8, pure RNA ~2.0. Low ratio indicates protein contamination.
- **A260/A230:** Should be 2.0-2.2. Low ratio indicates organic contaminant carryover
  (phenol, guanidine, EDTA).

---

## Luminescence — Reporter Gene Assays

### Overview

Luciferase reporter assays (firefly or Renilla). Enzyme catalyzes luciferin oxidation
producing light proportional to gene expression.

### Typical Settings

| Parameter | Value |
|-----------|-------|
| Read mode | Luminescence, endpoint |
| Integration time | 0.5-1.0 sec per well [UNVERIFIED] |
| Gain | 135 (or auto) [UNVERIFIED] |
| Plate format | 96-well white, opaque |
| Optics | Top read |

### Notes

- Use white opaque plates to maximize signal and minimize cross-talk.
- Flash luminescence (firefly) decays rapidly; read within 10 minutes of substrate
  addition.
- Glow luminescence (stabilized substrates) is stable for 30+ minutes.
