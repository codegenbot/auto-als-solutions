```
def eat(hungry, needed, remaining):
    eaten = min(min(needed, hungry), remaining)
    return [eaten, remaining - eaten]