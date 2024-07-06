Here's the solution to the problem:

```Python
def eat(hungry, needed, remaining):
    eaten = min(needed, min(hungry, remaining))
    return [eaten, needed - eaten]