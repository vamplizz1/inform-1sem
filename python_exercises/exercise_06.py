a = list(map(int, input().split()))
for number in a:
    if a.count(number) == 1:
        print(number, end=' ')
print()
