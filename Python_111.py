def histogram(test):
    if not test:
        return {}
    letter_count = {}
    for letter in test.split():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    max_count = max(letter_count.values())
    most_repeated_letters = [
        letter for letter, count in letter_count.items() if count == max_count
    ]
    return {
        letter: count
        for letter, count in letter_count.items()
        if letter in most_repeated_letters
    }