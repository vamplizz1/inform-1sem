data = list(map(int, input().split()))
n = data[0]
while len(data) < n:
    data.extend(map(int, input().split()))

missing = 0
for number in range(1, n + 1):
    missing ^= number
for i in range(1, n):
    missing ^= data[i]
print(missing)
