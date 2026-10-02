import random
import numpy as np


def generate_data(n, a, b, sigma=1.0):
    if n < 2:
        raise ValueError('Для определения прямой нужны хотя бы две точки.')
    if sigma < 0:
        raise ValueError('Разброс не может быть отрицательным.')
    x = np.arange(n, dtype=float)
    noise = np.array([random.gauss(0, sigma) for _ in range(n)])

    dx = x - x.mean()
    noise -= noise.mean()
    noise -= dx * (np.dot(dx, noise) / np.dot(dx, dx))
    y = a * x + b + noise
    return x, y


if __name__ == '__main__':
    n, a, b = input().split()
    x, y = generate_data(int(n), float(a), float(b))
    for xi, yi in zip(x, y):
        print(xi, yi)
