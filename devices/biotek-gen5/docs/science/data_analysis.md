# Plate Reader Data Analysis — Principles

**Source:** Standard biostatistics and assay development references.

## Blank Subtraction

The first step in any plate reader data analysis. Blank wells contain everything
except the analyte of interest.

```
Value_corrected = Value_raw - Mean(blank_wells)
```

### Blank Well Convention

- **Columns 11-12** (or last two columns) are commonly used as blanks in 96-well assays.
- Blanks should contain all reagents except the analyte (substrate only, no sample).
- Use at minimum 2 replicates of blanks; 4-8 replicates preferred.

### When to Flag Blanks

- Individual blank value > 2 SD from blank mean: outlier, consider excluding.
- Blank mean > 0.1 OD (absorbance): possible contamination or insufficient washing.

## Replicates and Precision

### Coefficient of Variation (CV%)

```
CV% = (Standard_Deviation / Mean) * 100
```

| CV% | Interpretation |
|-----|---------------|
| < 5% | Excellent reproducibility |
| 5-10% | Good |
| 10-15% | Acceptable (flag for review) |
| 15-25% | Problematic (investigate cause) |
| > 25% | Unreliable (repeat assay) |

### Replicate Requirements

| Assay Type | Minimum Replicates | Recommended |
|------------|-------------------|-------------|
| Standards | 2 | 3 |
| Samples | 2 | 3 |
| Controls | 2 | 4 |
| Blanks | 2 | 4-8 |

## Standard Curves

### Linear Regression

For assays with a linear response over the working range:

```
y = mx + b
```

Where y = signal, x = concentration, m = slope, b = intercept.
Use when R-squared > 0.99 over the desired range.

### 4-Parameter Logistic (4PL)

The gold standard for immunoassays (ELISA) with sigmoidal dose-response:

```
y = D + (A - D) / (1 + (x / C)^B)
```

Where:
- **A** = minimum asymptote (response at zero concentration)
- **B** = Hill slope (steepness of the curve)
- **C** = EC50 / IC50 (inflection point, concentration at half-max response)
- **D** = maximum asymptote (response at infinite concentration)

### 5-Parameter Logistic (5PL) [UNVERIFIED]

Extension of 4PL with an asymmetry parameter:

```
y = D + (A - D) / (1 + (x / C)^B)^S
```

Where S is the asymmetry factor. Use when the dose-response curve is not symmetric
around the inflection point.

### Choosing a Curve Fit

| Curve Type | When to Use |
|-----------|-------------|
| Linear | Nucleic acid quantification, Bradford (narrow range) |
| 4PL | ELISA, most immunoassays |
| 5PL | Asymmetric dose-response curves [UNVERIFIED] |
| Polynomial | Rarely; when biological model is unknown |
| Point-to-point | Last resort; no interpolation beyond standards |

## Assay Quality Metrics

### Z-Factor (Z')

A statistical measure of assay quality for screening applications:

```
Z' = 1 - (3 * SD_positive + 3 * SD_negative) / |Mean_positive - Mean_negative|
```

| Z' Value | Interpretation |
|----------|---------------|
| 1.0 | Ideal (zero variability) |
| 0.5 - 1.0 | Excellent assay |
| 0.0 - 0.5 | Marginal assay (may need optimization) |
| < 0.0 | Unusable (signal and noise overlap) |

### Signal-to-Background Ratio (S/B)

```
S/B = Mean_signal / Mean_background
```

A S/B > 3 is generally acceptable. S/B > 10 is desirable for quantitative work.

### Signal-to-Noise Ratio (S/N)

```
S/N = (Mean_signal - Mean_background) / SD_background
```

A S/N > 10 provides reliable quantification.

## Dose-Response Analysis

### IC50 / EC50

- **IC50:** Concentration that produces 50% inhibition (e.g., drug screening).
- **EC50:** Concentration that produces 50% of maximum effect.
- Calculated from the inflection point (parameter C) of a 4PL fit.
- Report with confidence interval and Hill slope.

### Percent Activity / Inhibition

```
% Activity = (Sample - Negative_Control) / (Positive_Control - Negative_Control) * 100
% Inhibition = 100 - % Activity
```

## Gen5 Built-in Analysis [UNVERIFIED]

Gen5 includes data reduction capabilities within protocols:

- Blank subtraction (automatic)
- Standard curve fitting (linear, 4PL, log-logit)
- Concentration calculation for unknowns
- Kinetic rate calculation (Vmax, time-to-threshold)
- Spectral peak identification
- Well flagging based on QC criteria
