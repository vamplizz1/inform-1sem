n = int(input())
a = list(map(int, input().split()))
for candidate in a:
    less = 0
    for number in a:
        if number < candidate:
            less += 1
    if less == n // 2:
        print(candidate)
        break
