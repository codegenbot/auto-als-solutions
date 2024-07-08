def bowling_score(frames):
    score = 0
    frames = frames.split('/')
    for i in range(len(frames)):
        frame = frames[i]
        if len(frame) == 1:
            score += 10
        elif len(frame) == 2:
            first_roll = int(frame[0])
            second_roll = int(frame[1])
            if first_roll + second_roll == 10:
                score += 10
            else:
                score += first_roll + second_roll
        else:
            rolls = [int(x) for x in frame.replace('-', '').replace('/', '')]
            if len(rolls) > 2 or 'X' in frame or str(sum(rolls)) + '/' in frame:
                strike_bonus = sum([10] + rolls[:1])
                score += strike_bonus
            else:
                score += sum(rolls)
    return score

print(bowling_score("7/3/5/5/10/0/1/7/6/4"))