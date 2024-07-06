def split_words(txt):
    words = txt.split()
    if len(words) > 0 and all(char.isalnum() for char in words[0]):
        return [word for word in words]
    else:
        try:
            return words
        except ValueError:
            return sum(1 for char in txt.lower() if ord(char) % 2 == 1)