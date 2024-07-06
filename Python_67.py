```
def fruit_distribution(s, n):
    s = s.replace("apples", "a").replace("oranges", "o")
    a_count = s.count('a')
    o_count = s.count('o')
    return max(0, n - (int("".join(filter(str.isdigit, s))) + a_count + o_count))