import numpy as np


def solve_system(augmented):
    augmented = np.asarray(augmented, dtype=float)
    if augmented.ndim != 2 or augmented.shape[1] < 2:
        raise ValueError('Нужны коэффициенты хотя бы одной переменной и столбец правых частей.')
    coefficients = augmented[:, :-1]
    constants = augmented[:, -1]
    solution, _, rank, _ = np.linalg.lstsq(coefficients, constants, rcond=None)
    if not np.allclose(coefficients @ solution, constants, rtol=1e-9, atol=1e-9):
        return None, None

    _, _, vh = np.linalg.svd(coefficients, full_matrices=True)
    basis = vh[rank:].T
    return solution, basis


if __name__ == '__main__':
    n, m = map(int, input().split())
    rows = []
    for _ in range(n):
        row = list(map(float, input().split()))
        if len(row) != m:
            raise ValueError('Количество чисел в строке должно равняться M.')
        rows.append(row)
    solution, basis = solve_system(rows)
    if solution is None:
        print('Решений нет.')
    elif basis.shape[1] == 0:
        print(*solution)
    else:
        print('Бесконечно много решений.')
        print('Частное решение:', *solution)
        print('Общее решение: частное решение + t1*v1 + t2*v2 + ...')
        print('Параметры t — произвольные действительные числа.')
        for i in range(basis.shape[1]):
            print(f'v{i + 1}:', *basis[:, i])
