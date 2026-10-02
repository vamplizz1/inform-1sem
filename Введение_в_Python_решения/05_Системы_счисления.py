data = input().split()
while len(data) < 3:
    data.extend(input().split())
n = data[0]
b = int(data[1])
c = int(data[2])

number = int(n, b)
result = ''
while number > 0:
    result = str(number % c) + result
    number //= c
print(result or '0')
