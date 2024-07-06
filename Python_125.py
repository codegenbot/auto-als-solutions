def split_words(txt):
    words = txt.split()
    if not any(char in word for word in words for char in ",.!?"):
        return [word for word in words if word[0].islower()]
    else:
        return words