def bowling_score(bowling_round):
    score = 0
    roll = [0] * 10
    i = j = 0
    for frame in bowing_round:
        if frame == "X":
            score += 10
            i += 1
        elif "/" in frame:
            a, b = map(int, frame.split("/"))
            score += a + b
            i += 1
            roll[i] = min(a, b)
        else:
            a = int(frame)
            score += a
            i += 1
            roll[i] = a
    if i < 10:
        for k in range(i + 1, 11):
            if sum(roll[:k]) == 10:
                score += 10
            else:
                score += roll[k]
    return score