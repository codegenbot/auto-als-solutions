def histogram(test):
    from collections import Counter

    words = test.split()
    counter = Counter(words)
    max_count = max(counter.values())
    return {k: v for k, v in counter.items() if v == max_count}