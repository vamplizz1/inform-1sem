with open('input.txt', encoding='utf-8') as file:
    numbers = list(map(float, file.readline().split()))
    operation = file.readline().strip()

result = numbers[0]
for number in numbers[1:]:
    if operation == '+':
        result += number
    elif operation == '-':
        result -= number
    elif operation == '*':
        result *= number

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(str(result))
