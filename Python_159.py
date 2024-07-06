```
def eat(hungry, needed, remaining):
    return [min(remaining, min(needed, hungry)), needed - min(remaining, min(needed, hungry))]