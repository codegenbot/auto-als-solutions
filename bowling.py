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
                    score += 10
                elif int(split_frame[0]) + int(split_frame[1]) >= 10:
                    spare = True
                    score += int(split_frame[0]) + int(split_frame[1])
                else:
                    score += sum(map(int, split_frame))
                if strike or spare and i < 9:
                    try:
                        score += int(frames[i+1]) + int(frames[i+2])
                    except IndexError:
                        pass
        else:
            score += int(frames[i])
    return score