```
def split_words(txt):
    words = txt.split()
    if len(words) > 0 and any(char.isalpha() for char in words[0]):
        return words
    elif ',' in txt:
        return txt.split(',')
    else:
        result = 0
        for i, c in enumerate(txt.lower()):
            if 'a' <= c <= 'z':
                if (i + ord('a')) % 2 == 1:
                    result += 1
        return result