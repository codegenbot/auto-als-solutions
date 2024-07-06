def eat(number, need, remaining):
    if remaining < need:
        eaten = min(remaining, need)
    else:
        eaten = min(1000, need + (number - remaining))
    return [eaten, max(0, remaining - (need - eaten))]