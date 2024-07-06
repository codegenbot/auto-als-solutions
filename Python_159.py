def eat(number, need, remaining):
    total_eaten = min(number + need, remaining)
    return [total_eaten, max(remaining - total_eaten, 0)]