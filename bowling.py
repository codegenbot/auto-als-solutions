def bowling_score(frames):
    score = 0
    frames = frames.split(' ')
    for i in range(0, len(frames), 2):
        if '/' not in frames[i]:
            score += int(frames[i])
        else:
            split_frame = list(map(int, frames[i].split('/')))
            if sum(split_frame) == 10:
                score += 10
            elif split_frame[0] + split_frame[1] == 10:
                score += 10
            else:
                score += sum(split_frame)
    return score