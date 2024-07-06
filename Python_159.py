def eat(number, need, remaining):
    eaten = min(1000, number + (need - remaining)) if remaining >= need else need
    return [eaten, max(0, remaining - (need - eaten))]