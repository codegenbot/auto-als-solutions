```
def split_words(txt):
    words = txt.split()
    if len(words) > 0:
        return words
    else:
        word_list = txt.replace(",", " ").split()
        if len(word_list) > 0:
            return word_list
        else:
            odd_count = sum(1 for c in txt.lower() if ord(c) % 2 == 1)
            return odd_count