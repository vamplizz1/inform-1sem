import string
import unicodedata
from pathlib import Path


def top_words(text, limit=10):
    text = ''.join(' ' if ch in string.punctuation or unicodedata.category(ch).startswith('P')
                   else ch for ch in text.lower())
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]


if __name__ == '__main__':
    filename = input('Путь к текстовому файлу: ').strip()
    text = Path(filename).expanduser().read_text(encoding='utf-8')
    for word, count in top_words(text):
        print(word, count)
