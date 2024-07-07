def bowling_score(frames):
    score = 0
    frames = frames.split(' ')
    for i in range(10):
        if '/' in frames[i]:
            split_frame = list(map(int, frames[i].split('/')))
            if sum(split_frame) == 10:
                score += 10 + sum(split_frame)
            elif max(split_frame) == 10:
                score += 10 + min(split_frame)
            else:
                score += sum(split_frame)
        else:
            score += int(frames[i])
    return score