Here is the completed code:

def compare(game,guess):
    return [abs(guess[i]-game[i]) for i in range(len(game))]