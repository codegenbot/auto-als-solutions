def bowling_score(frames):
    score = 0
    frames_list = frames.split()
    for i in range(0, len(frames_list), 2):
        if '/' in frames_list[i]:
            split_frame = list(map(int, frames_list[i].split('/')))
            if sum(split_frame) == 10:
                score += 10 + sum(split_frame)
            else:
                score += 10
                score += sum(split_frame)
        else:
            score += int(frames_list[i])
    return score