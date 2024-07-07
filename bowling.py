def bowling_score(frames):
    score = 0
    roll = 0
    for frame in frames.split("/"):
        if len(frame) == 1:
            if int(frame) < 10:
                score += int(frame)
            else:
                score += 10 + 10
            roll += 2
        elif len(frame) == 2:
            first_roll = int(frame[0])
            second_roll = int(frame[1])
            if first_roll + second_roll == 10:
                score += 10
                roll += 2
            else:
                score += first_roll + second_roll
                roll += 2
        else:
            score += 10
            roll += 2
    return score