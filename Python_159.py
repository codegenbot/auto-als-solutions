def eat(number, need, remaining):
    if remaining >= need:
        return [number + (need - remaining), 0]
    else:
        return [number + remaining, remaining - number]