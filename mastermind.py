def mastermind(code, guess):
    correct_colors = [c1 == c2 for c1, c2 in zip(code, guess)]
    black_pegs = sum([c1 == c2 and idx1 == idx2 for idx1, (c1, c3), idx2, (c2, c4) in enumerate(zip(code, guess))])
    
    white_pegs = sum(correct_colors) - black_pegs
    return str(white_pegs) + "\n" + str(black_pegs)

print(mastermind("RRRR", "RRRR"))
print(mastermind("BOYG", "GYOB"))
print(mastermind("WYYW", "BBOG"))
print(mastermind("GGGB", "BGGG"))
print(mastermind("BBBB", "OOOO"))