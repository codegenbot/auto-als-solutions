```
def eat(number, need, remaining):
    if remaining < need:
        total_eaten = need
        remaining -= (need - number)
    else:
        total_eaten = min(need, number) + (need - remaining)
    return [total_eaten, remaining - total_eaten]