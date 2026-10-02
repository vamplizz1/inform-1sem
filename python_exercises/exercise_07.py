a = list(map(int, input().split()))
answer = a[0]
max_count = 0
for number in a:
    count = a.count(number)
    if count > max_count:
        max_count = count
        answer = number
print(answer)
