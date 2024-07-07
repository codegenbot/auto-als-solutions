def mastermind(code, guess):
    code_counts = [0] * 6
    for char in code:
        code_counts[ord(char) - ord("A")] += 1

    white_pegs = sum(
        min(count, guess.count(char)) for count, char in zip(code_counts, "ABCDEF")
    )

    black_pegs = sum(
        c == g and code_counts[i] > 0 for i, (c, g) in enumerate(zip(code, guess))
    )

    return str(white_pegs) + "\n" + str(black_pegs)