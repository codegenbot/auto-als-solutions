def fruit_distribution(s, n):
    s = s.replace("apples and", "apples ").replace("oranges", "oranges ")
    n_apples = int(s.split(" ")[0].split(" ")[-1].strip())
    return n - n_apples