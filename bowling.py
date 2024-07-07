```
def bowling_score(frames):
    score = 0
    for i in range(10):
        if '/' in frames[i]:
            split_frame = frames[i].split('/')
            if len(split_frame) > 1:
                strike = False
                spare = False
                if int(split_frame[0]) == 10:
                    strike = True
                elif int(split_frame[0]) + int(split_frame[1]) >= 10:
                    spare = True
                score += 10
                if not strike and not spare:
                    score += sum(map(int, split_frame))
        else:
            score += int(frames[i])
    return score