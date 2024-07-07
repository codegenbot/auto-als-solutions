def bowling_score(frames):
    score = 0
    for i in range(10):
        if "/" in frames[i]:
            split_frame = frames[i].split("/")
            if len(split_frame) > 1:
                if int(split_frame[0]) == 10:
                    score += 10 + 10 * (9 - i)
                elif int(split_frame[0]) + int(split_frame[1]) == 10:
                    score += 10 + int(frames[i + 1])
        else:
            score += int(frames[i])
    return score