def mastermind(code, guess):
    white = sum(
        c1 == c2 and i != j
        for i, (c1, _) in enumerate(guess)
        for j, (_, c2) in enumerate(code)
    )
    black = sum((c1, i) in zip(code, range(4)) for i, (c1, _) in enumerate(guess))
    return str(white), str(black)