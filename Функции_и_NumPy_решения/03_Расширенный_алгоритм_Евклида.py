import sys


def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = extended_gcd(b, a % b)
    return y, x - (a // b) * y, d


def best_coefficients(a, b):
    x0, y0, d = extended_gcd(a, b)
    step_x = b // d
    step_y = a // d


    k1 = (-x0) // step_x
    k2 = y0 // step_y
    candidates = []
    for k in (k1, k1 + 1, k2, k2 + 1):
        x = x0 + step_x * k
        y = y0 - step_y * k
        candidates.append((abs(x) + abs(y), x, y))
    _, x, y = min(candidates)
    return x, y, d


if __name__ == '__main__':
    for line in sys.stdin:
        if line.strip():
            a, b = map(int, line.split())
            print(*best_coefficients(a, b))
