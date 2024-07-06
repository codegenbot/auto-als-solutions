def eat(number, need, remaining):
    eaten = min(number, need)
    return [eaten, max(0, remaining - (need - eaten))]