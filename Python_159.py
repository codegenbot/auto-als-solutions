```
def eat(hungry, needed, remaining):
    eaten = min(remaining, min(needed, hungry))
    return [eaten, remaining - eaten]

print(eat(5, 3, 2))  # Output: [1, 1]