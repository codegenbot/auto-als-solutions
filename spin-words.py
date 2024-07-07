def spin_words(text):
    words = text.split()
    result = []

    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.insert(0, word)

    return " ".join(result)