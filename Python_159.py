def eat(number, need, remaining):
    eaten = min(need, remaining) if remaining < need else min(1000, remaining + (need - remaining))
    return [eaten, max(0, remaining - (need - eaten))]