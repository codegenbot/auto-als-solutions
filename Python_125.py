```
def split_words(txt):
    words = txt.split()
    if any(char in words[0] for char in ',.!'):
        return [words[0]]
    else:
        odd_count = sum(1 for c in txt.lower() if ord(c) % 2 != 0)
        return odd_count