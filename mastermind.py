def mastermind(code, guess):
    black_pegs = sum(c == g for c, g in zip(code, guess))
    white_pegs = (
        sum(min(code.count(x), guess.count(x)) for x in set("ROYGBW")) - black_pegs
    )
    return white_pegs, black_pegs


code = input().strip()
guess = input().strip()
white_pegs, black_pegs = mastermind(code, guess)
print(white_pegs)
print(black_pegs)