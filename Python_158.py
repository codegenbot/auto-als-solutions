def find_max(words):
    max_word = None
    for word in words:
        if not max_word or len(set(word)) > len(set(max_word)):
            max_word = word
    return min(
        [word for word in words if len(set(word)) == len(set(max_word))], key=min
    )