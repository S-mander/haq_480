"""Simple visualization for HAQ bitwidth strategies"""
import matplotlib.pyplot as plt


def visualize_strategy(strategy, save_path, linear_quantization=False):
    """Visualize bitwidth strategy as a simple bar chart"""
    if linear_quantization:
        # Linear: [[w_bit, a_bit], ...]
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        weights = [s[0] for s in strategy]
        activations = [s[1] if s[1] != -1 else 0 for s in strategy]

        ax1.bar(range(len(weights)), weights)
        ax1.set_title('Weight Bitwidths')
        ax1.set_ylabel('Bits')

        ax2.bar(range(len(activations)), activations)
        ax2.set_title('Activation Bitwidths')
        ax2.set_ylabel('Bits')
        ax2.set_xlabel('Layer')

    else:
        # K-Means: [bit, bit, bit, ...]
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.bar(range(len(strategy)), strategy)
        ax.set_title('Bitwidth per Layer')
        ax.set_xlabel('Layer')
        ax.set_ylabel('Bits')

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
