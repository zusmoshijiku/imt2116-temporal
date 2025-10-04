# Symbolic Regression Methods for Oceanic Modeling

Repository for the Capstone project. September - December 2025.

## Repository Structure (ideal)

```bash
sr-capstone/
├─ README.md                       # quickstart + roadmap   mapped to the plan
├─ LICENSE
├─ environment.yml                 # pinned env (python + libs)
├─ .pre-commit-config.yaml         # black, isort, flake8, nbstripout
├─ .github/
│  ├─ workflows/ci.yml             # tests + lint + tiny smoke runs
│  ├─ ISSUE_TEMPLATE/
│  │  ├─ task.md                   # atomic task (with DoD)
│  │  ├─ experiment.md             # GP / PySR / Operon / EQL runs
│  │  └─ rfc.md                    # design changes (operators, losses, etc.)
│  └─ PULL_REQUEST_TEMPLATE.md     # metrics table + plots + repro cmd
├─ docs/
│  ├─ plan.md                      # project overview
│  ├─ milestone_m1_report.md       # “First report/presentation”
│  └─ slides/                      # reveal.js, pptx, pdf
├─ literature/
│  ├─ papers.bib
│  ├─ reading-notes/               # 1 page notes (aprox) per paper
│  └─ templates/reading-note.md
├─ notes/                          # weekly notes (YYYY-WW-Name.md)
├─ src/
│  └─ sr/
│     ├─ core/                     # trees, safe ops, simplifier
│     ├─ gp/                       # GP-SR toy engine
│     ├─ baselines/                # PySR, Operon, gplearn wrappers
│     ├─ diff/                     # differentiable SR (templates + const opt)
│     ├─ eval/                     # metrics (R²/MSE/MAE, MDL, TED, entropy)
│     ├─ plots/                    # pareto, knee, stability, quality-vs-budget
│     └─ utils/                    # config, seeds, logging
├─ experiments/
│  ├─ run.py                       # CLI: python -m experiments.run --config ...
│  └─ configs/
│     ├─ gp/*.yaml
│     ├─ baselines/*.yaml          # aligned operator sets/budgets
│     └─ diff/*.yaml
├─ data/                           
└─ results/                        # metrics.json + plots per run (gitignored)
```

## Work Overview

1. Problem and Background Study 
   1. Symbolic Regression
   2. Biological Context
2. Learn to use and evaluate existing libraries (PySR, gplearn, Operon/PyOperon)
   1. Libraries documentation
   2. Toy implementation (consider: synthetic tabular data)
3. Literature Review
   1. Milestone: Define Approach. Create initial report (or presentation)
4. Approach
5. Results
6. Create Report