import csv
import random
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


def load_films(path):
    with open(path, encoding='utf-8-sig', newline='') as file:
        reader = csv.DictReader(file)
        if not {'Title', 'Genre'}.issubset(reader.fieldnames or []):
            raise ValueError('Нужны столбцы Title и Genre.')
        return [row for row in reader if row.get('Title') and row.get('Genre')]


def matching_films(films, genre):
    return [film for film in films if genre.strip().casefold() in
            {part.strip().casefold() for part in film['Genre'].split('|')}]


def create_app():
    root = tk.Tk()
    root.title('Фильмотека')
    root.minsize(480, 290)
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill='both', expand=True)
    films = []
    genre = tk.StringVar()
    result = tk.StringVar(value='Выберите жанр')
    ttk.Label(frame, text='Жанр').pack(anchor='w')
    combo = ttk.Combobox(frame, textvariable=genre, width=35)
    combo.pack(fill='x', pady=8)

    def read_file(path):
        try:
            loaded = load_films(path)
            if not loaded:
                raise ValueError('В файле нет фильмов.')
            films[:] = loaded
            genres = sorted({part.strip() for film in films for part in film['Genre'].split('|')})
            combo['values'] = genres
            genre.set(genres[0])
            result.set(f'Загружено фильмов: {len(films)}')
        except (OSError, ValueError, csv.Error) as error:
            messagebox.showerror('Ошибка файла', str(error), parent=root)

    def choose_file():
        path = filedialog.askopenfilename(parent=root, filetypes=[('CSV', '*.csv')])
        if path:
            read_file(path)

    def choose_film(event=None):
        candidates = matching_films(films, genre.get())
        if not candidates:
            result.set('Фильмы этого жанра не найдены.')
            return
        film = random.choice(candidates)
        result.set(f"{film['Title']} ({film.get('Year', '—')})\n"
                   f"{film['Genre']}\nРейтинг IMDb: {film.get('IMDB rating', '—')}")

    ttk.Button(frame, text='Выбрать фильм', command=choose_film).pack(pady=6)
    ttk.Button(frame, text='Открыть CSV', command=choose_file).pack(pady=6)
    ttk.Label(frame, textvariable=result, wraplength=450, justify='center').pack(pady=16)
    root.bind('<Return>', choose_film)
    path = Path(__file__).resolve().with_name('imdb_top_250.csv')
    if path.exists():
        read_file(path)
    return root


if __name__ == '__main__':
    create_app().mainloop()
