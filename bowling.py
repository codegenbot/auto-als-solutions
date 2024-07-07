def bowling_score(frames):
    score = 0
    frame_list = frames.split()
    for i in range(0, len(frame_list), 2):
        if '/' in frame_list[i]:
            split_frame = list(map(int, frame_list[i].split('/')))
            if sum(split_frame) == 10:
                score += 10 + sum(split_frame)
            else:
                score += 10 + min(split_frame)
        else:
            score += sum(map(int, (frame_list[i], frame_list[i+1])))
    return score