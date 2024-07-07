def mastermind(code, guess):
    code_counts = [0] * 6
    for c in code:
        code_counts[ord(c) - ord("A")] += 1

    white_pegs = sum(
        min(count, g.count(c)) for c, count in zip(map(ord, code), map(ord, guess))
    )

    black_pegs = sum(
        1 for c, count in zip(code, guess) if c == chr(ord(c) - ord("A") + 1)
    )

    return str(black_pegs) + "\n" + str(4 - black_pegs)