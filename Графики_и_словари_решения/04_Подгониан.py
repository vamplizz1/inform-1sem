from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


FOLDER = Path(__file__).resolve().parent if '__file__' in globals() else Path.cwd()

from itertools import combinations

data = pd.read_csv(FOLDER / 'iris_data.csv')
columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
names = ['Длина чашелистника, см', 'Ширина чашелистника, см',
         'Длина лепестка, см', 'Ширина лепестка, см']
fig, axes = plt.subplots(2, 3, figsize=(16, 9), layout='constrained')
results = []
for ax, (i, j) in zip(axes.flat, combinations(range(4), 2)):

    pair = data[[columns[i], columns[j]]].apply(pd.to_numeric).dropna()
    x = pair[columns[j]].to_numpy()
    y = pair[columns[i]].to_numpy()
    if len(x) < 2 or np.ptp(x) == 0:
        raise ValueError('Для МНК нужны хотя бы два различных значения x.')
    a, b = np.polyfit(x, y, 1)
    r = np.corrcoef(x, y)[0, 1] if np.ptp(y) else float('nan')
    grid = np.linspace(x.min(), x.max(), 100)
    ax.scatter(x, y, s=18, alpha=0.65, label='Наблюдения')
    ax.plot(grid, a*grid+b, color='crimson', label=f'МНК, r = {r:.2f}')
    ax.set(xlabel=names[j], ylabel=names[i])
    ax.grid(alpha=0.25)
    ax.legend()
    print(f'{columns[i]} = {a:.6f} * {columns[j]} + {b:.6f}; r = {r:.6f}')
    results.append((abs(r), columns[i], columns[j], r))
valid = [item for item in results if np.isfinite(item[0])]
if valid:
    _, y_name, x_name, r = max(valid)
    direction = 'положительная' if r >= 0 else 'отрицательная'
    print(f'Наибольшая по модулю корреляция: {y_name} и {x_name}, r={r:.3f}.')
    print(f'Связь {direction}; корреляция не доказывает причинную зависимость.')
fig.suptitle('Шесть пар признаков ирисов и прямые МНК')
fig.savefig(FOLDER / '04_Подгониан.png', dpi=180)
plt.show()
