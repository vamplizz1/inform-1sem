from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


FOLDER = Path(__file__).resolve().parent if '__file__' in globals() else Path.cwd()

data = pd.read_csv(FOLDER / 'iris_data.csv')
species = data['Species'].value_counts()
lengths = pd.to_numeric(data['PetalLengthCm'], errors='raise').dropna()

counts = [(lengths <= 1.2).sum(),
          ((lengths > 1.2) & (lengths <= 1.5)).sum(),
          (lengths > 1.5).sum()]
labels = ['L ≤ 1.2 см', '1.2 < L ≤ 1.5 см', 'L > 1.5 см']
if species.empty or sum(counts) == 0:
    raise ValueError('Нет данных для круговых диаграмм.')
fig, axes = plt.subplots(1, 2, figsize=(12, 5), layout='constrained')
axes[0].pie(species.values, labels=species.index, autopct='%1.1f%%', startangle=90)
axes[0].set_title('Доли видов ирисов')
axes[1].pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
axes[1].set_title('Доли по длине лепестка: непересекающиеся группы')

for label, mask in [('L > 1.2', lengths > 1.2),
                    ('1.2 < L < 1.5', (lengths > 1.2) & (lengths < 1.5)),
                    ('L > 1.5', lengths > 1.5)]:
    print(f'{label}: {mask.sum()} из {len(lengths)} ({mask.mean():.1%})')
fig.savefig(FOLDER / '03_Пироги_с_цветами.png', dpi=180)
plt.show()
