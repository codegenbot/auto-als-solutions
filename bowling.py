def bowling_score(frames):
    score = 0
    frame_count = 0
    for frame in frames:
        if '/' in frame:
            split_frame = list(map(int, frame.split('/')))
            if sum(split_frame) == 10:
                score += 10
            else:
                score += sum(split_frame)
        else:
            score += int(frame)
        frame_count += 1
    return score