```
def longest_word_with_max_unique_chars(words):
    max_word = ''
    max_unique_chars = 0
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_unique_chars:
            max_unique_chars = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_unique_chars:
            if len(word) > len(max_word):
                max_word = word
    return max_word