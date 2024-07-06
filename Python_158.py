Here is the corrected code:

def find_max(words):
    max_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_word = word
            max_length = len(word)
        elif len(word) == max_length and word > max_word:
            max_word = word
    return max_word