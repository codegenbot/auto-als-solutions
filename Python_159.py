def eat(number, need, remaining):
    if number < remaining:
        eaten = remaining
    elif number >= need:
        eaten = need
    else:
        eaten = min(number, need)
    return [eaten, max(0, need - eaten)]