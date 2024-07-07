def leaders(input):
    return [
        x
        for i, x in enumerate(reversed(input))
        if x >= all(map(lambda y: int(y) < x, input[i + 1 :]))
    ]