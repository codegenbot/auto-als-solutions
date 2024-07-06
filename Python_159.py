def eat(number, need, remaining):
    total_eaten = number + need - remaining if remaining >= need else number + remaining
    return [total_eaten, abs(total_eaten - (number + need))]