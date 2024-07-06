def eat(number, need, remaining):
    eaten = min(need, number)
    return [eaten, max(0, remaining - (need - eaten))]