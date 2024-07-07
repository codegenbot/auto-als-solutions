Here is the solution:

def mastermind(code, guess):
    white = sum(c in guess for c in code)
    black = 4 - sum((code[i] == guess[i]) for i in range(4))
    return str(black) + "\n" + str(white)