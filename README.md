# E-PAS IoT Sensor Synchronization

This repository contains the public reproducibility package for the manuscript:

**E-PAS: A Privacy-Budget-Aware and Energy-Efficient State Synchronization Framework for Distributed IoT Sensor Networks**

## Repository Scope

The package is intended to support manuscript review and figure/table verification. It includes:

- processed numerical results used in the main comparison and scalability tables;
- configuration notes and random-seed information for the reported simulation setting;
- standalone figure exports in PDF/PNG format;
- editable TikZ figure sources;
- the figure-generation script used to produce the polished scientific figures;
- the LaTeX manuscript source for the Sensors submission version.

The full raw simulation logs and expanded executable experiment materials are available from the corresponding author upon reasonable request.

## Directory Layout

```text
code/                 Plotting and figure-generation scripts
configs/              Experiment configuration and random-seed notes
data/processed/       Processed values used in manuscript tables and figures
environment/          Python dependency information
figures/              Standalone manuscript figures in PDF and PNG
figures_tikz/         Editable TikZ figure sources
manuscript/           LaTeX manuscript source
```

## Quick Start

Create a Python environment and install the plotting dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r environment/requirements.txt
python code/generate_polished_figures.py
```

The script writes regenerated figures to `figures_polished/` in the working directory.

## Citation

If you use this package, please cite the manuscript after publication. A provisional citation metadata file is provided in `CITATION.cff`.

## Availability Statement

Processed results, configuration notes, random-seed information, manuscript source files, and figure-generation assets are available in this repository. Full raw simulation logs and expanded executable experiment materials are available from the corresponding author upon reasonable request.
