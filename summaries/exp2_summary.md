# Summary of EXP2

Experiment 2: Training on synthetic noisy data.

This experiment builds upon EXP1 by introducing Gaussian noise to the synthetic dataset to stress-test model robustness under perturbations.

**Results Overview:** After 30 epochs, the model achieved a training accuracy of 0.98 and validation accuracy of 0.96. The final training loss was 0.02 and validation loss was 0.05. Convergence was slower relative to the baseline.

**Interpretation:** Noise in the data increases difficulty and slows convergence slightly. This highlights the importance of stress testing models under varied conditions. The results illustrate how experimental scaffolding can surface stability issues and inform model improvements without exposing proprietary algorithms.
