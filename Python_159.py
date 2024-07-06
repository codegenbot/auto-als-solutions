def eat(hungry, needed, remaining):
    eaten = min(remaining, min(needed, hungry))
    return [eaten, remaining - eaten]