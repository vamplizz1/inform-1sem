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
x = (data['date'] - data['date'].min()).dt.total_seconds().to_numpy() / 86400
if len(np.unique(x)) < 4:
    raise ValueError('Для полинома третьей степени нужны хотя бы 4 различные даты.')

center = x.mean()
scale = np.ptp(x)
t = (x-center) / scale
coefficients = np.polyfit(t, data['close'].to_numpy(), 3)
polynomial = np.poly1d(coefficients)
grid = np.linspace(x.min(), x.max(), 1000)
dates = data['date'].min() + pd.to_timedelta(grid, unit='D')
fig, ax = plt.subplots(figsize=(12, 5), layout='constrained')
ax.plot(data['date'], data['close'], linewidth=1, alpha=0.7, label='Цена закрытия')
ax.plot(dates, polynomial((grid-center)/scale), linewidth=2,
        color='crimson', label='Полином третьей степени')
ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5, maxticks=9))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
ax.set(xlabel='Дата (ДД-ММ-ГГ)', ylabel='Цена закрытия, единицы исходного файла',
       title='Аппроксимация исторической цены биткоина')
ax.tick_params(axis='x', rotation=30)
ax.grid(alpha=0.3)
ax.legend()
print('Коэффициенты при t³, t², t, 1:', coefficients)
print(f't = (число дней от первой даты - {center}) / {scale}')
fig.savefig(FOLDER / '06_Полином_для_биткоина.png', dpi=180)
plt.show()
