import random

with open('input.txt', encoding='utf-8') as file:
    words = file.read().split()

if len(words) < 2:
    print('Для обучения нужно хотя бы два слова.')
else:
    transitions = {}
    for i in range(len(words) - 1):
        current = words[i]
        following = words[i + 1]
        if current not in transitions:
            transitions[current] = []
        transitions[current].append(following)

    current = random.choice(list(transitions))
    result = [current]
    for _ in range(49):
        if current not in transitions:
            break
        current = random.choice(transitions[current])
        result.append(current)

    generated = ' '.join(result)
    print(generated)
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(generated)
