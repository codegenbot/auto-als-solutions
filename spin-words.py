```
def spin_words(text):
    words = text.split()
    result = []

    for i, word in enumerate(words):
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
        words += [" "] if i < len(words) - 1 else ""

    return "".join(result)