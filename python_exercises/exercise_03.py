text = input().strip()
original = 'AHIMOTUVWXY18EJSZ3L25'
reflected = 'AHIMOTUVWXY183L25EJSZ'

palindrome = text == text[::-1]
mirrored = True
for i in range(len(text)):
    symbol = text[i]
    if symbol not in original or reflected[original.index(symbol)] != text[-1 - i]:
        mirrored = False
        break

if palindrome and mirrored:
    print(f'{text} is a mirrored palindrome.')
elif palindrome:
    print(f'{text} is a regular palindrome.')
elif mirrored:
    print(f'{text} is a mirrored string.')
else:
    print(f'{text} is not a palindrome.')
