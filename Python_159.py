def eat(hungry, needed, remaining):
    if needed > hungry and needed > remaining:
        return [hungry, 0]
    else:
        eaten = min(needed, min(hungry, remaining))
        return [eaten, needed - eaten]