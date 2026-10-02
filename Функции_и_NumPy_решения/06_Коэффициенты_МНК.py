import numpy as np


def least_squares(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.ndim != 1 or y.ndim != 1 or len(x) != len(y) or len(x) < 2:
        raise ValueError('Нужны два одномерных массива одинаковой длины, минимум 2 точки.')
    dx = x - x.mean()
    denominator = np.dot(dx, dx)
    if denominator == 0:
        raise ValueError('При одинаковых x коэффициенты прямой не определяются однозначно.')
    a = np.dot(dx, y - y.mean()) / denominator
    b = y.mean() - a * x.mean()
    return a, b


if __name__ == '__main__':
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    a, b = least_squares(x, y)
    print(a, b)
