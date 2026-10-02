g, text = input().split()
g = int(g)
size = len(text) // g
result = ''.join(text[i:i + size][::-1] for i in range(0, len(text), size))
print(result)
