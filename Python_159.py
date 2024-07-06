```
def eat(hungry, needed, remaining):
    eaten = min(min(hungry, needed), remaining)
    return [eaten, remaining - eaten]