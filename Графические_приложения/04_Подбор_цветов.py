import re
import tkinter as tk
from tkinter import ttk, colorchooser


def complementary(color):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', color):
        raise ValueError('Введите цвет в формате #RRGGBB.')
    return '#' + ''.join(f'{255 - int(color[i:i+2], 16):02x}' for i in (1, 3, 5))


def create_app():
    root = tk.Tk()
    root.title('Подбор цветов')
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill='both', expand=True)
    color = tk.StringVar(value='#00a3a6')
    result = tk.StringVar()
    ttk.Entry(frame, textvariable=color, width=25).grid(row=0, column=0, padx=8)
    canvas = tk.Canvas(frame, width=420, height=150, highlightthickness=0)
    canvas.grid(row=2, column=0, columnspan=2, pady=15)
    left = canvas.create_rectangle(0, 0, 210, 150, outline='')
    right = canvas.create_rectangle(210, 0, 420, 150, outline='')

    def update(event=None):
        try:
            original = color.get().strip().lower()
            opposite = complementary(original)
            canvas.itemconfigure(left, fill=original)
            canvas.itemconfigure(right, fill=opposite)
            result.set(f'{original}    →    {opposite}')
        except ValueError as error:
            result.set(str(error))

    def choose():
        initial = color.get().strip()
        if not re.fullmatch(r'#[0-9a-fA-F]{6}', initial):
            initial = '#ffffff'
        _, selected = colorchooser.askcolor(color=initial, parent=root)
        if selected:
            color.set(selected)
            update()

    ttk.Button(frame, text='Выбрать цвет', command=choose).grid(row=0, column=1)
    ttk.Button(frame, text='Подобрать', command=update).grid(row=1, columnspan=2, pady=10)
    ttk.Label(frame, textvariable=result).grid(row=3, columnspan=2)
    root.bind('<Return>', update)
    update()
    return root


if __name__ == '__main__':
    create_app().mainloop()
