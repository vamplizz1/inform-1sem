from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


FOLDER = Path(__file__).resolve().parent if '__file__' in globals() else Path.cwd()

import matplotlib.dates as mdates

def load_btc():
    data = pd.read_csv(FOLDER / 'BTC_data.csv')
    dates = pd.to_datetime(data.iloc[:, 0], errors='raise')
    prices = pd.to_numeric(data.iloc[:, -1], errors='raise')
    table = pd.DataFrame({'date': dates, 'close': prices}).dropna().sort_values('date')
    if table.empty:
        raise ValueError('В файле нет данных для графика.')
    return table

data = load_btc()
fig, ax = plt.subplots(figsize=(12, 5), layout='constrained')
ax.plot(data['date'], data['close'], linewidth=1, label='Цена закрытия')
ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5, maxticks=9))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
ax.set(xlabel='Дата (ДД-ММ-ГГ)', ylabel='Цена закрытия, единицы исходного файла',
       title='Историческая цена биткоина')
ax.tick_params(axis='x', rotation=30)
ax.grid(alpha=0.3)
ax.legend()
fig.savefig(FOLDER / '05_История_биткоина.png', dpi=180)
plt.show()
