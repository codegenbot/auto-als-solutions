```
def mastermind(code, guess):
    correct_colors = [c1 == c2 for c1, c2 in zip(code, guess)]
    black_pegs = sum([1 for i, j in zip(code, guess) if i == j])
    
    white_pegs = sum(correct_colors) - black_pegs
    return str(white_pegs) + "\n" + str(black_pegs)

print(mastermind("RRRR", "RRRR"))
print(mastermind("BOYG", "GYOB"))
print(mastermind("WYYW", "BBOG"))
print(mastermind("GGGB", "BGGG"))
print(mastermind("BBBB", "OOOO"))