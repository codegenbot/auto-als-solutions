def eat(number, need, remaining):
    if number >= need:
        return [need, 0]
    else:
        return [number + max(need - (remaining - number), 0), max(0, remaining - need)]