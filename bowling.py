def bowling_score(frames):
    score = 0
    frame_index = 0
    while frame_index < len(frames):
        if '/' in frames[frame_index]:
            split_frame = list(map(int, frames[frame_index].split('/')))
            if sum(split_frame) == 10:
                score += 10 + sum(bowling_score(frames, frame_index+1))
            else:
                score += sum(split_frame)
                frame_index += 1
        else:
            score += int(frames[frame_index])
            frame_index += 1
    return score