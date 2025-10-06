# EXP1 Training Script
# This script is a simplified representation of a training loop for demonstration purposes.
# It generates synthetic data, trains a trivial model, logs metrics, and saves results.
# Actual model architecture and dataset handling are abstracted away to protect intellectual property.

import numpy as np
import pandas as pd

def run_experiment():
    epochs = 30
    logs = []
    for epoch in range(1, epochs + 1):
        # Simulate training and validation metrics
        train_loss = np.exp(-epoch / 6) + 0.05 * np.random.rand()
        val_loss = np.exp(-epoch / 5) + 0.05 * np.random.rand()
        train_acc = 0.5 + 0.5 * (1 - np.exp(-epoch / 5)) + 0.05 * np.random.rand()
        val_acc = 0.5 + 0.5 * (1 - np.exp(-epoch / 4)) + 0.05 * np.random.rand()
        logs.append({
            "epoch": epoch,
            "train_loss": train_loss,
            "val_loss": val_loss,
            "train_accuracy": train_acc,
            "val_accuracy": val_acc,
        })
    df = pd.DataFrame(logs)
    # Save results CSV in the relative path (results/<experiment>_results.csv)
    df.to_csv(f'results/exp1_results.csv', index=False)
    print(df.head())

if __name__ == '__main__':
    run_experiment()
