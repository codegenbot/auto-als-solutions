def eat(number, need, remaining):
    eaten = min(min(number, remaining), need)
    return [eaten, max(0, need - eaten)]