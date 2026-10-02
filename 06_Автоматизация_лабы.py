import csv
import math
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


def load_data(path):
    with open(path, encoding='utf-8-sig', newline='') as file:
        sample = file.read(4096)
        file.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=',;\t')
        except csv.Error:
            dialect = csv.excel
        rows = [row for row in csv.reader(file, dialect) if any(value.strip() for value in row)]
    if not rows or len(rows[0]) < 2:
        raise ValueError('В CSV нужны как минимум два столбца: x и y.')
    names = ('x', 'y')
    try:
        float(rows[0][0].replace(',', '.'))
        float(rows[0][1].replace(',', '.'))
    except ValueError:
        names = tuple(rows.pop(0)[:2])
    x, y = [], []
    for row in rows:
        if len(row) < 2:
            raise ValueError('В каждой строке нужны x и y.')
        a, b = float(row[0].replace(',', '.')), float(row[1].replace(',', '.'))
        if not math.isfinite(a) or not math.isfinite(b):
            raise ValueError('Значения должны быть конечными числами.')
        x.append(a)
        y.append(b)
    return x, y, names


def fit_line(x, y):
    if len(x) != len(y) or len(x) < 2:
        raise ValueError('Нужно не менее двух пар измерений.')
    mx, my = sum(x)/len(x), sum(y)/len(y)
    denominator = sum((value-mx)**2 for value in x)
    if denominator == 0:
        raise ValueError('Значения x не должны быть одинаковыми.')
    a = sum((xi-mx)*(yi-my) for xi, yi in zip(x, y)) / denominator
    return a, my-a*mx


def save_plot(path, x, y, names):
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    a, b = fit_line(x, y)
    figure = Figure(figsize=(8, 5), layout='constrained')
    FigureCanvasAgg(figure)
    ax = figure.add_subplot(111)
    ax.scatter(x, y, label='Измерения')
    ends = [min(x), max(x)]
    ax.plot(ends, [a*v+b for v in ends], color='crimson', label=f'y = {a:.4g}x + {b:.4g}')
    ax.set(xlabel=names[0], ylabel=names[1], title='Линейная аппроксимация МНК')
    ax.grid(alpha=0.3)
    ax.legend()
    figure.savefig(path, dpi=180)
    return a, b


def create_app():
    root = tk.Tk()
    root.title('Автоматизация лабораторной работы')
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill='both', expand=True)
    state = {}
    status = tk.StringVar(value='Выберите CSV: первые два столбца — x и y.')
    result = tk.StringVar()

    def choose():
        path = filedialog.askopenfilename(parent=root, filetypes=[('CSV', '*.csv')])
        if not path:
            return
        try:
            x, y, names = load_data(path)
            fit_line(x, y)
            state.update(x=x, y=y, names=names)
            status.set(f'{Path(path).name} — измерений: {len(x)}')
            result.set('')
            button.configure(state='normal')
        except (OSError, ValueError, csv.Error) as error:
            messagebox.showerror('Ошибка данных', str(error), parent=root)

    def process():
        a, b = fit_line(state['x'], state['y'])
        result.set(f'a = {a:.6g}\nb = {b:.6g}')
        path = filedialog.asksaveasfilename(parent=root, defaultextension='.png',
                    initialfile='Аппроксимация.png', filetypes=[('PNG', '*.png')])
        if path:
            try:
                save_plot(path, state['x'], state['y'], state['names'])
                status.set(f'График сохранён: {path}')
            except (ImportError, OSError, ValueError) as error:
                messagebox.showerror('Ошибка сохранения', str(error), parent=root)

    ttk.Button(frame, text='Выбрать CSV', command=choose).pack(pady=8)
    button = ttk.Button(frame, text='Вычислить МНК и сохранить график', command=process, state='disabled')
    button.pack(pady=8)
    ttk.Label(frame, textvariable=status, wraplength=480).pack(pady=10)
    ttk.Label(frame, textvariable=result, font=('', 16)).pack(pady=10)
    return root


if __name__ == '__main__':
    create_app().mainloop()
