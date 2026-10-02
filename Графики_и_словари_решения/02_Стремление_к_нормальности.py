from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


FOLDER = Path(__file__).resolve().parent if '__file__' in globals() else Path.cwd()

rng = np.random.default_rng(42)
sizes = [100, 1000, 10000, 100000]
sample = rng.normal(0, 1, sizes[-1])
bins = np.linspace(-5, 5, 51)
x = np.linspace(-5, 5, 500)
density = np.exp(-x*x/2) / np.sqrt(2*np.pi)
fig, axes = plt.subplots(2, 2, figsize=(11, 7), sharex=True, sharey=True,
                         layout='constrained')
for ax, size in zip(axes.flat, sizes):
    ax.hist(sample[:size], bins=bins, density=True, alpha=0.65, label='Выборка')
    ax.plot(x, density, color='crimson', label='Плотность N(0, 1)')
    ax.set(title=f'N = {size}', xlabel='Значение', ylabel='Плотность')
    ax.grid(alpha=0.2)
    ax.legend()
fig.suptitle('Нормальное распределение: увеличение объёма выборки')
fig.savefig(FOLDER / '02_Стремление_к_нормальности.png', dpi=180)
plt.show()
