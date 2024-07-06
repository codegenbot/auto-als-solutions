def eat(number, need, remaining):
    total_eaten = number + min(need - remaining, 0)
    return [total_eaten, remaining - total_eaten]