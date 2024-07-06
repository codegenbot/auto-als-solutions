def eat(number, need, remaining):
    return [
        min(number + (need - remaining), number) if remaining >= need else number,
        remaining - max(0, remaining - need),
    ]