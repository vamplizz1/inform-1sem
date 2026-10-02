import math
import tkinter as tk
from tkinter import ttk


def calculate_bmi(weight, height_cm):
    if not all(math.isfinite(v) and v > 0 for v in (weight, height_cm)):
        raise ValueError('Введите положительные массу и рост.')
    bmi = weight / (height_cm / 100) ** 2
    if bmi <= 16:
        category = 'Выраженный дефицит массы тела'
    elif bmi < 18.5:
        category = 'Недостаточная масса тела'
    elif bmi < 25:
        category = 'Норма'
    elif bmi < 30:
        category = 'Избыточная масса тела'
    elif bmi < 35:
        category = 'Ожирение I степени'
    elif bmi < 40:
        category = 'Ожирение II степени'
    else:
        category = 'Ожирение III степени'
    return bmi, category


def create_app():
    root = tk.Tk()
    root.title('Индекс массы тела')
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill='both', expand=True)
    weight, height, result = tk.StringVar(), tk.StringVar(), tk.StringVar()
    for row, (label, variable) in enumerate([('Масса, кг', weight), ('Рост, см', height)]):
        ttk.Label(frame, text=label).grid(row=row, column=0, sticky='w', pady=8)
        ttk.Entry(frame, textvariable=variable, width=22).grid(row=row, column=1, padx=12)

    def submit(event=None):
        try:
            bmi, category = calculate_bmi(float(weight.get().replace(',', '.')),
                                          float(height.get().replace(',', '.')))
            result.set(f'ИМТ: {bmi:.2f} кг/м²\n{category}')
        except (ValueError, OverflowError, ZeroDivisionError):
            result.set('Проверьте массу и рост: нужны положительные числа.')

    ttk.Button(frame, text='Рассчитать', command=submit).grid(row=2, columnspan=2, pady=12)
    ttk.Label(frame, textvariable=result, wraplength=360).grid(row=3, columnspan=2, pady=8)
    ttk.Label(frame, text='Для взрослых. Ориентировочная оценка, не диагноз.',
              wraplength=360).grid(row=4, columnspan=2, pady=8)
    root.bind('<Return>', submit)
    return root


if __name__ == '__main__':
    create_app().mainloop()
