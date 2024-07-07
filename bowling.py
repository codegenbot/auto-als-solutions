def bowling_score(frames):
    score = 0
    for i in range(10):
        if '/' in frames[i]:
            split_frame = list(map(int, frames[i].split('/')))
            score += sum(split_frame)
            if sum(split_frame) == 10:
                if len(split_frame) > 1:
                    score += sum(list(map(int, frames[i+1:i+2])))
                else:
                    score += sum(list(map(int, frames[i+1:i+3])))
        else:
            score += int(frames[i])
    return score