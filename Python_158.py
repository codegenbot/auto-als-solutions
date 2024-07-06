def longest_word_with_unique_characters(words):
    max_word = ''
    max_length = 0
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_length:
            max_length = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_length:
            max_word = min(max_word, word)
    return max_word