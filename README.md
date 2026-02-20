# Experimentation Toolkit

A modular Python toolkit for designing and analyzing A/B experiments using statistical testing, power analysis, and revenue impact estimation.

---

# Overview

This project simulates real-world experimentation workflows used in product-based companies to evaluate feature changes and make data-driven rollout decisions.

It answers key experimentation questions:

- Is the lift statistically significant?
- What is the effect size?
- How many users are required for the experiment?
- What is the revenue and profit impact?

---

# Project Structure

```
experimenttoolkit/
│
├── ABSimulator/
│   ├── __init__.py
│   ├── ab_test.py
│   ├── power_analysis.py
│   ├── revenue_analysis.py
│   ├── visualisation.py
│
├── run_experiment.py
├── requirements.txt
└── README.md
```

---

# Example Usage

```python
from ABSimulator.ab_test import run_ab_test

results = run_ab_test(
    n_control=5000,
    n_treatment=5000,
    p_control=0.10,
    p_treatment=0.12
)

print(results)
```

---

# Features

- Two-Proportion Z-Test
- Confidence Intervals
- Absolute & Relative Lift Calculation
- Power & Sample Size Estimation
- Revenue & Profit Impact Analysis
- Visualization of Experiment Results

---

# Tech Stack

- Python
- NumPy
- Statsmodels
- Matplotlib

---

# Purpose

This toolkit demonstrates practical understanding of:

- Hypothesis testing
- Experiment design
- Statistical power
- Business impact analysis
- Modular Python project structure