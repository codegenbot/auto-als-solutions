def bowling_score(frames):
    score = 0
    frames = [int(x) if x.isdigit() else x for x in frames.replace('-', '')]
    for i, frame in enumerate(frames):
        if frame == 'X':
            score += 10
            if i < 9 and frames[i+1] in ['X', '10']:
                score += frames[i+1]
            elif i < 9:
                score += frames[i+2]
        elif frame == '10':
            score += 10
            continue
        elif len(str(frame)) > 1:
            first_roll = int(frame[0])
            second_roll = int(frame[1])
            if first_roll + second_roll == 10:
                score += 10
            else:
                score += first_roll + second_roll
        else:
            score += frame
    return score

frames = "7/3/5/5/10/0/1/7/6/4"
print(bowling_score(frames))