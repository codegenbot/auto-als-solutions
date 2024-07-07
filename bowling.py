def bowling_score(frames):
    score = 0
    current_frame = 0
    for frame in frames.split():
        if '/' in frame:
            split_frame = list(map(int, frame.split('/')))
            if sum(split_frame) == 10:
                score += 10
                current_frame += 1
            else:
                score += sum(split_frame)
                current_frame += 1
                if current_frame < 10:
                    if split_frame[0] + sum(list(map(int, frames.split()[current_frame].split('/')))[:1]) >= 10:
                        score += 10 - split_frame[0]
                    else:
                        score += sum(list(map(int, frames.split()[current_frame].split('/'))))
        else:
            score += int(frame)
            current_frame += 1
    return score