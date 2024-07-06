def fruit_distribution(s, n):
    s = s.replace("apples", "a").replace("oranges", "o")
    return n - int(
        "".join(filter(str.isdigit, s)).translate({ord("a"): "", ord("o"): ""})
    )