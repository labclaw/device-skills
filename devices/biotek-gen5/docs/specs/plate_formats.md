# Microplate Formats — Synergy H1 Compatible

**Source:** SBS/ANSI standards and common laboratory practice.
Items marked [UNVERIFIED] need confirmation.

## Supported Plate Formats

The Synergy H1 accepts SBS-standard microplates (127.76 x 85.48 mm footprint).

| Format | Wells | Rows x Cols | Well Volume (uL) | Typical Use |
|--------|-------|-------------|-------------------|-------------|
| 6-well | 6 | 2 x 3 | 2000-5000 | Cell culture, large-volume assays |
| 12-well | 12 | 3 x 4 | 1000-4000 | Cell culture |
| 24-well | 24 | 4 x 6 | 500-3000 | Cell culture, medium-throughput |
| 48-well | 48 | 6 x 8 | 500-1500 | Medium-throughput screening |
| 96-well | 96 | 8 x 12 | 100-300 | Standard assays (most common) |
| 384-well | 384 | 16 x 24 | 20-100 | High-throughput screening |

## 96-Well Plate Types

| Plate Type | Color | Bottom | Use Case |
|------------|-------|--------|----------|
| Clear flat-bottom | Clear | Clear | Absorbance reads (ELISA, Bradford) |
| Black clear-bottom | Black | Clear | Fluorescence (bottom read, reduced cross-talk) |
| Black opaque | Black | Black | Fluorescence (top read only) |
| White opaque | White | White | Luminescence (maximizes light collection) |
| UV-transparent | Clear | UV-clear | Nucleic acid quantification (260 nm) |
| Half-area | Clear | Clear | Low-volume absorbance (50 uL reads) [UNVERIFIED] |

## Well Geometry

### 96-Well Standard (Full Area)

| Property | Value |
|----------|-------|
| Well diameter | 6.86 mm (top), 6.35 mm (bottom) [UNVERIFIED] |
| Well depth | 11.2 mm [UNVERIFIED] |
| Well spacing | 9.0 mm center-to-center |
| Typical assay volume | 100-200 uL |
| Minimum read volume | 50 uL (absorbance), 100 uL (fluorescence) [UNVERIFIED] |
| Path length at 200 uL | ~5.7 mm [UNVERIFIED] |

### 384-Well Standard

| Property | Value |
|----------|-------|
| Well spacing | 4.5 mm center-to-center |
| Typical assay volume | 25-80 uL |
| Minimum read volume | 20 uL [UNVERIFIED] |

## Path Length Correction

For absorbance readings, the measured OD depends on the optical path length through the
sample. In a microplate, path length varies with volume (unlike a standard 1 cm cuvette).

Gen5 can apply path length correction to normalize readings to a 1 cm equivalent:

- Uses a ratio of absorbance at 900 nm and 977 nm to calculate water path length
  [UNVERIFIED]
- Correction factor: `OD_corrected = OD_measured * (1.0 / path_length_cm)` [UNVERIFIED]
- Enable in Gen5 protocol under Read Step > Advanced > Path Length Correction

## Edge Effect Considerations

Wells at the plate perimeter (row A, row H, column 1, column 12) are prone to:

- **Evaporation artifacts** — edge wells lose volume faster during long incubations at
  elevated temperature (>2 hours at 37C).
- **Temperature gradients** — edge wells equilibrate faster with ambient temperature.
- **Mitigation:** Use plate sealers, humidified incubators, or leave edge wells empty.
