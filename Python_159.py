def eat(number, need, remaining):
    eaten = number + (need - remaining) if remaining >= need else need
    return [eaten, remaining - (need - eaten)] if eaten <= 1000 and remaining - (need - eaten) >= 0 else [-1, -1]