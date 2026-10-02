with open('input.txt', encoding='utf-8') as file:
    tokens = file.readline().split()
    operation = file.readline().strip()
    base = int(file.readline())

numbers = [int(token, base) for token in tokens]
result = numbers[0]
for number in numbers[1:]:
    if operation == '+':
        result += number
    elif operation == '-':
        result -= number
    elif operation == '*':
        result *= number


digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sign = '-' if result < 0 else ''
number = abs(result)
answer = ''
while number > 0:
    answer = digits[number % base] + answer
    number //= base
answer = sign + (answer or '0')

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(answer)
