# Summary of EXP1

Experiment 1: Baseline training on synthetic data.

This experiment simulates a standard supervised learning setup on synthetic data. The goal is to demonstrate typical training dynamics with decreasing loss and increasing accuracy.

**Results Overview:** After 30 epochs, the model achieved a training accuracy of 1.01 and validation accuracy of 0.99. The final training loss was 0.01, while the validation loss was 0.04. See the plot in the `plots` directory for accuracy curves.

**Interpretation:** The training curves show a consistent decrease in loss and increase in accuracy. In exp1, the presence of noise slows convergence slightly, highlighting the importance of stress testing for robustness. These results illustrate how experimental scaffolding can surface stability issues and inform model improvements without exposing proprietary algorithms.
