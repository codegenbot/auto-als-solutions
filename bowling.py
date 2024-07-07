def bowling_score(frames):
    score = 0
    frame_index = 0
    for i in range(1, 11):
        if '/' in frames[frame_index:frame_index+2]:
            split_frame = list(map(int, frames[frame_index:frame_index+2].split('/')))
            frame_index += 2
            if sum(split_frame) == 10:
                score += 10 + sum(split_frame)
            else:
                score += sum(split_frame)
        elif int(frames[frame_index]) < 10:
            score += int(frames[frame_index])
            frame_index += 1
        else:
            score += 10
            frame_index += 1
    return score