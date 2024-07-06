def eat(number, need, remaining):
    eaten = min(number, need)
    if number > need:
        return [eaten, max(0, remaining - (need - eaten))]
    else:
        return [number, max(0, remaining + (need - number))]