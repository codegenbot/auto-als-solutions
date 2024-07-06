def eat(hungry, needed, remaining):
    eaten = min(needed, min(hungry, remaining))
    return [eaten, needed - eaten]

assert eat(4, 5, 1) == [1, 0]