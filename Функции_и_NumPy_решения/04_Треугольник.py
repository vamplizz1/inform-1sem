def print_triangle(size, symb):
    for i in range(size):
        width = min(i + 1, size - i)
        print(symb * width)


if __name__ == '__main__':
    size, symb = input().split()
    print_triangle(int(size), symb)
