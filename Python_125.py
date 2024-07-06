def split_words(txt):
    words = txt.split()
    if any(char in word for word in words for char in ",.!"):
        return words
    else:
        odd_count = 0
        for i in range(26):
            if ord("a" + i) <= ord(
                c := next((c for c in txt.lower() if "a" <= c <= "z"), "")
            ):
                odd_count += 1
        return odd_count