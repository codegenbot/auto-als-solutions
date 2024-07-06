```
def split_words(txt):
    words = txt.split()
    if len(words) > 0:
        return words
    words = txt.replace(',', ' ')
    if len(words.split()) > 0:
        return words.split()
    return sum(1 for c in txt.lower() if ord(c) % 2 == 1 and ord('a') <= ord(c) <= ord('z'))