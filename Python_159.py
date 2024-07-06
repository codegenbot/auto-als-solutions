def eat(hungry, needed, remaining):
    eaten = min(remaining, min(needed, hungry))
    return [eaten, needed - eaten]