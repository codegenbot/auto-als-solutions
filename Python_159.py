def eat(number, need, remaining):
    eaten = min(number, min(need, remaining))
    return [eaten, max(0, need - eaten)]