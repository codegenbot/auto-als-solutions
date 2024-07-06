def eat(number, need, remaining):
    if number < remaining:
        eaten = min(number, need - remaining)
    else:
        eaten = min(number, need)
    return [eaten, max(0, need - eaten)]