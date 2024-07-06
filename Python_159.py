Here is the completed code:

def eat(number, need, remaining):
    total_eaten = number + (need - remaining) if remaining >= need else number + remaining
    carrots_left = max(0, remaining - (need - remaining)) if remaining >= need else 0
    return [total_eaten, carrots_left]