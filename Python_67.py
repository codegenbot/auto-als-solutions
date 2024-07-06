def fruit_distribution(s, n):
    words = s.split()
    for i in range(len(words)):
        if words[i].lower() == "apples" or words[i].lower() == "oranges":
            if words[i - 1].replace(".", "").isdigit():
                return (
                    n
                    - int(words[i - 1])
                    - int("".join(filter(str.isdigit, words[i + 2 :])))
                )