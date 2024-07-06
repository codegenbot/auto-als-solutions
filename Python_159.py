def eat(number, need, remaining):
    if number < need and number < remaining:
        eaten = number
    elif number >= need and number > remaining:
        eaten = remaining
    else:
        eaten = min(number, need)
    return [eaten, max(0, need - eaten)]