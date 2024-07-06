def eat(number, need, remaining):
    total_eaten = number + max(0, need - (remaining - number))
    return [total_eaten, min(need, remaining) - total_eaten]