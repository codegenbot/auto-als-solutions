```
def bowling_score(game):
    score = 0
    roll = 0
    for frame in game.split('/'):
        if len(frame) == 1:
            score += 10 + (10 - int(frame[0])) * 2
            continue
        elif len(frame) > 1 and frame[0] != 'X':
            score += sum(map(int, frame))
        else:
            score += 10 + (10 - int(frame[0])) * 2
        roll += 1
        if roll < 10:
            if len(frame) == 1 or frame[0] == 'X':
                continue
            elif int(frame[0]) + int(frame[-1]) == 10:
                score += sum(map(int, frame))
            else:
                score += sum(map(int, frame)) + 10
        roll %= 2
    return score