numbers = list(map(float, input().split()))
if not numbers:
    print('Введите хотя бы одно число.')
elif min(numbers) < 0:
    print('Среднее геометрическое определяем для неотрицательных чисел.')
else:
    product = 1
    for number in numbers:
        product *= number
    print(product ** (1 / len(numbers)))
