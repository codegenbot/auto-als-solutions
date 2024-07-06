def eat(number, need, remaining):
    if number < need:
        total_eaten = need
    else:
        total_eaten = number
    return [total_eaten, remaining - total_eaten]