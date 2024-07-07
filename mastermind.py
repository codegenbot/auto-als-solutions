def mastermind(code, guess):
    correct_place = sum(
        c1 == c2 and i1 == i2
        for i1, c1 in enumerate(guess)
        for i2, c2 in enumerate(code)
    )
    correct_color = sum(
        c1 in code and c1 != c2 for i, c1 in enumerate(guess) for c2 in code
    )
    return str(correct_place), str(4 - correct_place + correct_color)