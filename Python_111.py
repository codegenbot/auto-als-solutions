def histogram(test):
    if not test:
        return {}

    freq = {}
    max_freq = 0
    most_frequent = []

    for char in test.split():
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

        if freq[char] > max_freq:
            max_freq = freq[char]
            most_frequent = [char]
        elif freq[char] == max_freq:
            most_frequent.append(char)

    return {k: v for k, v in freq.items() if v == max_freq}