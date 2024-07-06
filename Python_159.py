def eat(number, need, remaining):
    if number < remaining:
        eaten = remaining
    else:
        eaten = min(number, need)
    return [eaten, max(0, need - eaten)]