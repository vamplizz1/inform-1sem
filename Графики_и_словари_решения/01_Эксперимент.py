from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


FOLDER = Path(__file__).resolve().parent if '__file__' in globals() else Path.cwd()


voltage = np.array([1, 2, 3, 4, 5, 6], dtype=float)
current = np.array([0.11, 0.19, 0.31, 0.39, 0.51, 0.60])
a, b = np.polyfit(voltage, current, 1)
x = np.linspace(0, 6.5, 200)
fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')
ax.errorbar(voltage, current, xerr=0.05, yerr=0.02, fmt='o', capsize=4,
            label='Учебные данные с погрешностями')
ax.plot(x, a*x+b, label=f'МНК: I = {a:.3f}U + {b:.3f}')
ax.set(xlabel='Напряжение U, В', ylabel='Сила тока I, А',
       title='Зависимость силы тока от напряжения')
ax.grid(alpha=0.3)
ax.legend()
print(f'a = {a}, b = {b}')
fig.savefig(FOLDER / '01_Эксперимент.png', dpi=180)
plt.show()
