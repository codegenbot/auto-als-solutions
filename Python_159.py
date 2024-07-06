```
def eat(hungry, needed, remaining):
    if needed > hungry + remaining:
        return [hungry, 0]
    eaten = min(needed, min(hungry, remaining))
    return [eaten, needed - eaten]