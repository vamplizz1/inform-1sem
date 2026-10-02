with open('input.txt', encoding='utf-8') as file:
    text = file.read()

vowels = 'аеёиоуыэюя'
consonants = 'бвгджзйклмнпрстфхцчшщ'
parts = []
for i, symbol in enumerate(text):
    parts.append(symbol)
    current = symbol.lower()
    if current in vowels:
        previous = text[i - 1].lower() if i > 0 else ' '
        following = text[i + 1].lower() if i + 1 < len(text) else ' '
        isolated = previous not in vowels and following not in vowels
        if isolated or previous in consonants:
            parts.append('с' + current)

result = ''.join(parts)
print(result)
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(result)
