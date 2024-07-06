def by_length(words):
    result = []
    for word in words:
        if len(word) >= 4:
            result.append(word)
    return result