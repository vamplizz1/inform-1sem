def prime_factors(n):
    if n < 1:
        raise ValueError('Введите натуральное число.')
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == '__main__':
    n = int(input())
    factors = prime_factors(n)
    if factors:
        print(*factors)
    else:
        print('У числа 1 нет простых множителей.')
