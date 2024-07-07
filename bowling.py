```
def bowling_score(s):
    score = 0
    roll = 0
    for frame in s.split('/'):
        if len(frame) == 1:
            score += 10
        elif 'X' in frame:
            score += 10 + (10 - int(frame.replace('X', '')))
        else:
            first_roll = int(frame[0])
            second_roll = 10 - first_roll
            if second_roll > int(frame[-1]):
                score += first_roll + second_roll
            else:
                score += first_roll + second_roll
        roll += 1
    return score