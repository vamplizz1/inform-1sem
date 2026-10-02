import random
import tkinter as tk
from tkinter import ttk


class Ball:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.radius = random.randint(10, 25)
        self.x = max(self.radius, min(x, canvas.winfo_width() - self.radius))
        self.y = max(self.radius, min(y, canvas.winfo_height() - self.radius))
        self.dx = random.choice([-4, -3, -2, 2, 3, 4])
        self.dy = random.choice([-4, -3, -2, 2, 3, 4])
        color = f'#{random.randrange(0x1000000):06x}'
        self.item = canvas.create_oval(0, 0, 0, 0, fill=color, outline='')
        self.draw()

    def draw(self):
        r = self.radius
        self.canvas.coords(self.item, self.x-r, self.y-r, self.x+r, self.y+r)

    def move(self):
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
        self.x += self.dx
        self.y += self.dy
        r = self.radius
        if self.x < r:
            self.x, self.dx = r, abs(self.dx)
        elif self.x > width-r:
            self.x, self.dx = width-r, -abs(self.dx)
        if self.y < r:
            self.y, self.dy = r, abs(self.dy)
        elif self.y > height-r:
            self.y, self.dy = height-r, -abs(self.dy)
        self.draw()


def create_app():
    root = tk.Tk()
    root.title('Шарики')
    root.minsize(350, 280)
    ttk.Label(root, text='Нажмите на поле, чтобы добавить шарик').pack(pady=10)
    canvas = tk.Canvas(root, width=600, height=400, bg='#f1f5f9', highlightthickness=0)
    canvas.pack(fill='both', expand=True)
    balls = []

    def add_ball(event):
        balls.append(Ball(canvas, event.x, event.y))

    def clear():
        balls.clear()
        canvas.delete('all')

    def tick():
        for ball in balls:
            ball.move()
        root.after(20, tick)

    canvas.bind('<Button-1>', add_ball)
    ttk.Button(root, text='Очистить', command=clear).pack(pady=8)
    tick()
    return root


if __name__ == '__main__':
    create_app().mainloop()
