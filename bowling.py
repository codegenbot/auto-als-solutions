def bowling_score(frames):
    score = 0
    for frame in frames.split('/'):
        if len(frame) == 1:
            score += 10
        elif len(frame) == 2:
            first_roll = int(frame[0])
            second_roll = int(frame[1])
            if first_roll + second_roll == 10:
                score += 10
            else:
                score += first_roll + second_roll
        elif len(frame) > 2:
            rolls = [int(x) for x in frame]
            score += sum(rolls)
    return score

frames = "7/3/5/5/10/0/1/7/6/4"
print(bowling_score(frames))