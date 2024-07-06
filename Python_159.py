```
def eat(number, need, remaining):
    if need > remaining:
        return [remaining, 0]
    else:
        return [number + max(need - (remaining - number), 0), max(0, remaining - need)]