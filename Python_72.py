def will_it_fly(q, w):
    return all(x == y for x, y in zip(q, q[::-1])) and sum(q) <= w