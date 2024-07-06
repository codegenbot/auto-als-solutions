def eat(hungry, needed, remaining):
    if hungry < remaining:
        eaten = min(needed, hungry)
    else:
        eaten = min(needed, remaining)
    return [eaten, needed - eaten]