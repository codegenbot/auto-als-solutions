```
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonants = 0
        for char in word.lower():
            if char.isalpha() and char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
                consonants += 1
        if consonants == n:
            result.append(word)
    return result