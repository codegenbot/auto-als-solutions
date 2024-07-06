def eat(number, need, remaining):
    eaten = number
    return [eaten, max(0, need - eaten)]