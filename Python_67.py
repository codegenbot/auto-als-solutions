```
def fruit_distribution(s, n):
    s = s.replace("apples", "a").replace("oranges", "o")
    digit_count = len("".join(filter(str.isdigit, s)))
    a_o_count = s.count('a') + s.count('o')
    return n - digit_count - a_o_count