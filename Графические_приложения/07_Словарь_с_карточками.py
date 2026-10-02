import random
import sqlite3
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox


class Dictionary:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.connection.execute('CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY, word TEXT NOT NULL, meaning TEXT NOT NULL)')
        self.connection.commit()

    def all(self):
        return self.connection.execute('SELECT id, word, meaning FROM words ORDER BY word COLLATE NOCASE').fetchall()

    def save(self, word, meaning, item_id=None):
        word, meaning = word.strip(), meaning.strip()
        if not word or not meaning:
            raise ValueError('Заполните слово и перевод.')
        with self.connection:
            if item_id is None:
                self.connection.execute('INSERT INTO words (word, meaning) VALUES (?, ?)', (word, meaning))
            else:
                self.connection.execute('UPDATE words SET word=?, meaning=? WHERE id=?', (word, meaning, item_id))

    def delete(self, item_id):
        with self.connection:
            self.connection.execute('DELETE FROM words WHERE id=?', (item_id,))

    def close(self):
        self.connection.close()


def create_app(db_path=None):
    database = Dictionary(db_path or Path(__file__).resolve().with_name('Словарь.db'))
    root = tk.Tk()
    root.title('Словарь с карточками')
    root.minsize(600, 450)
    tabs = ttk.Notebook(root)
    tabs.pack(fill='both', expand=True, padx=12, pady=12)
    edit = ttk.Frame(tabs, padding=12)
    study = ttk.Frame(tabs, padding=20)
    tabs.add(edit, text='Словарь')
    tabs.add(study, text='Карточки')
    tree = ttk.Treeview(edit, columns=('word', 'meaning'), show='headings', height=10, selectmode='browse')
    tree.heading('word', text='Слово')
    tree.heading('meaning', text='Перевод')
    tree.grid(row=0, column=0, columnspan=3, sticky='nsew')
    scroll = ttk.Scrollbar(edit, orient='vertical', command=tree.yview)
    scroll.grid(row=0, column=3, sticky='ns')
    tree.configure(yscrollcommand=scroll.set)
    edit.rowconfigure(0, weight=1)
    for i in range(3):
        edit.columnconfigure(i, weight=1)
    word, meaning = tk.StringVar(), tk.StringVar()
    selected = {'id': None}
    current = {'card': None}
    front = tk.StringVar(value='Добавьте слова и нажмите «Следующая»')
    back = tk.StringVar()
    ttk.Entry(edit, textvariable=word).grid(row=1, column=0, pady=12, sticky='ew')
    ttk.Entry(edit, textvariable=meaning).grid(row=1, column=1, columnspan=2, padx=8, sticky='ew')

    def refresh():
        tree.delete(*tree.get_children())
        for item_id, w, m in database.all():
            tree.insert('', 'end', iid=str(item_id), values=(w, m))
        current['card'] = None
        front.set('Нажмите «Следующая»')
        back.set('')

    def clear():
        selected['id'] = None
        tree.selection_remove(*tree.selection())
        word.set('')
        meaning.set('')

    def select(event=None):
        selection = tree.selection()
        if selection:
            selected['id'] = int(selection[0])
            w, m = tree.item(selection[0], 'values')
            word.set(w)
            meaning.set(m)

    def save():
        try:
            database.save(word.get(), meaning.get(), selected['id'])
            refresh()
            clear()
        except (ValueError, sqlite3.Error) as error:
            messagebox.showerror('Ошибка', str(error), parent=root)

    def delete():
        if selected['id'] is not None:
            database.delete(selected['id'])
            refresh()
            clear()

    def next_card():
        cards = database.all()
        if not cards:
            front.set('Словарь пока пуст')
            back.set('')
            current['card'] = None
            return
        card = random.choice(cards)
        current['card'] = card
        front.set(card[1])
        back.set('')

    def reveal():
        if current['card']:
            back.set(current['card'][2])

    tree.bind('<<TreeviewSelect>>', select)
    ttk.Button(edit, text='Новое слово', command=clear).grid(row=2, column=0, pady=8)
    ttk.Button(edit, text='Сохранить', command=save).grid(row=2, column=1, pady=8)
    ttk.Button(edit, text='Удалить выбранное', command=delete).grid(row=2, column=2, pady=8)
    ttk.Label(study, textvariable=front, font=('', 22), wraplength=500).pack(pady=25)
    ttk.Label(study, textvariable=back, font=('', 18), wraplength=500).pack(pady=20)
    ttk.Button(study, text='Показать перевод', command=reveal).pack(pady=8)
    ttk.Button(study, text='Следующая', command=next_card).pack(pady=8)

    def close():
        database.close()
        root.destroy()

    root.protocol('WM_DELETE_WINDOW', close)
    refresh()
    return root


if __name__ == '__main__':
    create_app().mainloop()
