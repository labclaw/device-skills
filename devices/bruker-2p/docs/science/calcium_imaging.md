# Calcium Imaging Methodology

> Background for AI agents analyzing two-photon calcium imaging data.

## Principle

Calcium imaging uses fluorescent indicators to report intracellular calcium
concentration ([Ca2+]i) as a proxy for neural activity. When a neuron fires an action
potential, voltage-gated calcium channels open and [Ca2+]i rises from ~50-100 nM to
~1-10 uM within milliseconds. Calcium indicators bind this calcium and increase their
fluorescence brightness, producing a measurable optical signal.

## Genetically Encoded Calcium Indicators (GECIs)

### GCaMP Family

GCaMP is the dominant GECI platform, based on circularly permuted GFP fused to
calmodulin and M13 peptide:

- **GCaMP6s** — "slow": rise ~180 ms, decay ~550 ms, highest sensitivity, detects
  single action potentials in ~95% of trials
- **GCaMP6f** — "fast": rise ~45 ms, decay ~140 ms, good temporal resolution
- **GCaMP7f** — improved SNR over 6f, similar kinetics
- **GCaMP8s** — highest sensitivity version, superior single-spike detection
- **GCaMP8f** — fast kinetics with sensitivity approaching 8s
- **GCaMP8m** — intermediate kinetics and sensitivity

### Delivery Methods

| Method | Expression Time | Cell Types | Permanence |
|--------|----------------|------------|------------|
| AAV injection | 2-4 weeks | Cre-dependent or pan-neuronal | Permanent |
| Transgenic mouse | Born with it | Defined by promoter | Permanent |
| Viral transduction (lentivirus) | 1-2 weeks | Broad | Permanent |
| In utero electroporation | Born with it | Layer-specific | Permanent |

Most common for systems neuroscience:
- **Ai148 x Cre driver** — transgenic cross for stable, cell-type-specific expression
- **AAV-Syn-GCaMP8s** — viral injection for pan-neuronal expression in specific regions

## Relationship: Calcium Transients to Neural Activity

### What Calcium Imaging Measures

- Each resolvable "calcium transient" corresponds to one or more action potentials
- **Single spike:** Small fluorescence increase (dF/F ~5-20% for GCaMP6f, ~20-50% for 8s)
- **Burst (5-10 spikes):** Large transient (dF/F ~50-300%)
- **Sustained activity:** Elevated plateau

### What It Does NOT Measure

- Subthreshold membrane potential changes
- Inhibitory (hyperpolarizing) events (calcium decreases are hard to detect)
- Individual spikes within a burst (temporal resolution limited by indicator kinetics
  and frame rate)
- Absolute firing rates (indicator saturation at high frequencies)

### Temporal Resolution Limits

| Frame Rate | GCaMP6f | GCaMP6s | GCaMP8f |
|-----------|---------|---------|---------|
| 30 Hz | ~7 spike resolution | ~2 spike resolution | ~10 spike resolution |
| 15 Hz | ~4 spike resolution | ~1 spike resolution | ~5 spike resolution |

"Spike resolution" = approximate number of distinct events separable per second
given indicator kinetics and frame rate.

## Typical Experimental Parameters

### Standard Calcium Imaging (Layer 2/3 Cortex)

| Parameter | Typical Value |
|-----------|---------------|
| Wavelength | 920 nm |
| Power at sample | 20-40 mW |
| Objective | 16x/0.8 NA water dipping |
| Zoom | 2-4x (200-400 um FOV) |
| Frame rate | 30 Hz (resonant galvo) |
| Resolution | 512x512 pixels |
| Duration | 5-30 minutes per trial |
| Depth | 150-350 um (layer 2/3) |
| Indicator | GCaMP6f, GCaMP7f, or GCaMP8f |
| PMT voltage | 600-800 V |

### Deep Imaging (Layer 5)

| Parameter | Typical Value |
|-----------|---------------|
| Wavelength | 920-940 nm |
| Power at sample | 60-120 mW |
| Depth | 450-650 um |
| Zoom | 2-3x |
| Frame rate | 30 Hz |
| Notes | Higher power needed; more scattering; lower SNR |

### Dual-Color Imaging (GCaMP + tdTomato)

| Parameter | Channel 1 (Green) | Channel 2 (Red) |
|-----------|-------------------|-----------------|
| Wavelength | 920 nm (excites both) | 920 nm (excites both) |
| Emission filter | 500-550 nm | 570-620 nm |
| Indicator | GCaMP8f | tdTomato (structural) |
| PMT voltage | 650 V | 550 V |

Note: At 920 nm, both GCaMP and tdTomato are excited (tdTomato has a broad 2P
absorption). For cleaner red channel, use 1040 nm, but this requires dual-laser setup.

## Analysis Pipeline

Standard calcium imaging analysis follows these stages:

### 1. Motion Correction

Brain motion from heartbeat and breathing must be corrected before signal extraction.

| Algorithm | Type | Speed | Quality | Tool |
|-----------|------|-------|---------|------|
| Rigid (translation) | Phase correlation | Fast | Good for small motion | suite2p, CaImAn |
| Non-rigid | Piecewise rigid | Slower | Better for large motion | suite2p, NoRMCorre |
| Template-based | Cross-correlation | Fast | Good | custom |

- suite2p uses a two-step approach: rigid registration first, then non-rigid refinement
- Typical brain motion: 1-5 um (well-fixed cranial window), 10-50 um (chronic window
  with some degradation)

### 2. ROI Detection (Cell Segmentation)

Identify individual neurons in the FOV:

| Method | Description | Tool |
|--------|-------------|------|
| Manual | Human draws ROIs | ImageJ/FIJI |
| Semi-auto | Correlation-based seeding + manual editing | suite2p |
| Fully auto | NMF-based simultaneous deconvolution | CaImAn (CNMF) |
| Deep learning | Trained segmentation network | Cellpose, suite2p (optional) |

suite2p and CaImAn are the dominant tools. Both output:
- ROI masks (binary or weighted)
- Fluorescence traces (raw F)
- Neuropil traces (background contamination estimate)

### 3. Signal Extraction

Extract fluorescence time series from each ROI:

```
F_cell(t) = mean pixel intensity within ROI at time t
F_neuropil(t) = mean intensity in surrounding annulus
F_corrected(t) = F_cell(t) - 0.7 * F_neuropil(t)   # neuropil correction
```

The neuropil correction factor (0.7) is empirically determined and may vary by
brain region and depth.

### 4. dF/F Computation

Normalize fluorescence to baseline:

```
F0 = percentile(F_corrected, 10)    # or rolling baseline
dF/F(t) = (F_corrected(t) - F0) / F0
```

dF/F is the standard unit for calcium imaging signals. Values:
- 0-10%: noise / quiet neuron
- 10-50%: single spikes or small bursts (depends on indicator)
- 50-300%: bursts or sustained activity
- >300%: strong bursts (may be saturated)

### 5. Spike Deconvolution (Optional)

Estimate the underlying spike train from the calcium trace:

| Algorithm | Description | Tool |
|-----------|-------------|------|
| OASIS | Fast non-negative deconvolution | CaImAn, suite2p |
| MLSpike | Bayesian spike inference | standalone (MATLAB) |
| CASCADE | Deep-learning deconvolution | CASCADE (Python) |

Deconvolution is useful for:
- Estimating firing rates
- Detecting individual spikes (for GCaMP8 at 30 Hz)
- Computing pairwise correlations between neurons

## Analysis Tools

### suite2p

- **Repository:** github.com/MouseLand/suite2p
- **Language:** Python
- **Pipeline:** registration -> detection -> extraction -> classification
- **GUI:** Built-in viewer for manual ROI curation
- **Input:** TIFF stacks (must combine single-page TIFFs first)
- **Output:** `stat.npy`, `F.npy`, `Fneu.npy`, `spks.npy`, `ops.npy`, `iscell.npy`

### CaImAn

- **Repository:** github.com/flatironinstitute/CaImAn
- **Language:** Python
- **Pipeline:** CNMF (constrained non-negative matrix factorization)
- **Strengths:** Simultaneous deconvolution and demixing, online processing
- **Input:** TIFF stacks or memory-mapped arrays
- **Output:** Spatial components (A), temporal components (C), deconvolved (S)

### DataJoint

- **Repository:** github.com/datajoint
- **Language:** Python
- **Purpose:** Data management pipeline (not analysis per se)
- **Element:** `element-calcium-imaging` provides standardized ingestion for
  suite2p and CaImAn outputs
- **PrairieView loader:** `element_interface.prairie_view_loader` handles
  Prairie XML parsing
