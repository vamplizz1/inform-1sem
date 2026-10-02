with open('input.txt', encoding='utf-8') as file:
    text = file.read()

count = 0
inside_ending = False
for symbol in text:
    if symbol in '.!?':
        if not inside_ending:
            count += 1
        inside_ending = True
    else:
        inside_ending = False
print(count)
