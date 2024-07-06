```
    def eat(hungry, needed, remaining):
        eaten = min(needed, min(hungry, remaining))
        return [eaten, needed - eaten]