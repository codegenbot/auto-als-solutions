def compare(game, guess):
    return [abs(a - b) if a != b else 0 for a, b in zip(game, guess)]