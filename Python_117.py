def select_words(s, n):
    words = s.split()
    result = [
        word
        for word in words
        if len([c for c in word if c.lower() not in "aeiou"]) == n
    ]
    return result