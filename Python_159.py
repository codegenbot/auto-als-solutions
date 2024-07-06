```
def eat(number, need, remaining):
    if number < need:
        eaten = number
    else:
        eaten = need
    return [eaten, max(0, remaining - (need - eaten))]