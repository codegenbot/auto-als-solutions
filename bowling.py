```
def bowling_score(frames):
    score = 0
    for i in range(10):
        if '/' in frames[i]:
            split_frame = list(map(int, frames[i].split('/')))
            if sum(split_frame) == 10:
                score += 10
            else:
                score += sum(split_frame)
                if sum(split_frame) < 10:
                    score += 10 - sum(split_frame)
        else:
            score += int(frames[i])
    return score