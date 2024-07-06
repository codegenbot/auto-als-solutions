```
def eat(number, need, remaining):
    if remaining >= need:
        eaten = min(1000, number + (need - remaining))
        return [eaten, remaining - (need - eaten)] if remaining - (need - eaten) >= 0 else [-1, -1]
    else:
        return [need, remaining - need] if remaining >= need else [-1, -1]