def eat(number, need, remaining):
    if number < remaining:
        eaten = min(number, need)
    else:
        eaten = min(number, remaining)
    return [eaten, max(0, need - eaten)]