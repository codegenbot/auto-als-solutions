```
def find_max(words):
    max_word = ''
    max_length = 0
    for word in words:
        length = len(set(word))
        if length > max_length or (length == max_length and word < max_word):
            max_word = word
            max_length = length
    return max_word