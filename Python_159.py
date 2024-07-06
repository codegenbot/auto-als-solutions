```
def eat(number, need, remaining):
    if number < need and number < remaining:
        eaten = number
        return [eaten, 0]
    elif need > remaining:
        eaten = remaining
        return [eaten, 0]
    else:
        eaten = min(number, need, remaining)
        return [eaten, max(0, need - eaten)]