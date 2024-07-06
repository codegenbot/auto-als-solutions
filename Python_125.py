```
def split_words(txt):
    words = txt.split()
    if len(words) > 0 and words[0].endswith(','):
        return [word.strip(',') for word in words]
    elif ',' not in txt:
        return sum(1 for char in txt if 'a' <= char <= 'z' and ord(char) % 2 == 1)
    else:
        return words