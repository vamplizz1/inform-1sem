import numpy as np


def spiral_matrix(n, m):
    matrix = np.zeros((n, m), dtype=int)
    top, bottom = 0, n - 1
    left, right = 0, m - 1
    value = 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            matrix[top, j] = value
            value += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i, right] = value
            value += 1
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom, j] = value
                value += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i, left] = value
                value += 1
            left += 1
    return matrix


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = spiral_matrix(n, m)

    result = matrix * np.arange(n)[:, None]
    for row in result:
        print(*row)
