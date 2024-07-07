def mastermind(code, guess):
    code_count = [0] * 6
    guess_count = [0] * 6
    black_pegs = 0
    white_pegs = 0

    for i in range(4):
        if code[i] == guess[i]:
            black_pegs += 1
        else:
            code_count[ord(code[i]) - ord("A")] += 1
            guess_count[ord(guess[i]) - ord("A")] += 1

    for i in range(6):
        if code_count[i] > 0 and code_count[i] != black_pegs:
            white_pegs += min(code_count[i], guess_count[i])

    return str(black_pegs) + "\n" + str(white_pegs)