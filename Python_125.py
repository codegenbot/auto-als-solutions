```
def split_words(txt):
    words = txt.split()
    if any(char.isalnum() for char in txt) and any(char.isdigit() or char.isalpha() for char in txt):
        return words
    elif ',' in txt:
        return txt.split(',')
    else:
        odd_count = sum(1 for i, c in enumerate(txt.lower()) if 'a' <= c <= 'z' and (i+ord('a')) % 2 == 1)
        return odd_count