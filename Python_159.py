def eat(number, need, remaining):
    total_eaten = need if number < need else number
    return [total_eaten, remaining - total_eaten]