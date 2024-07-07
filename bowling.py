```python
def bowling_score(frames):
    score = 0
    frame_count = 0
    for i in range(10):
        if '/' in frames[i]:
            split_frame = list(map(int, frames[i].split('/')))
            if sum(split_frame) == 10:
                score += 10
                frame_count -= 1
            else:
                score += sum(split_frame)
        else:
            score += int(frames[i])
        frame_count += 1
    while frame_count < 10 and any(map(lambda x: '/' in x, frames[frame_count+1:])):
        next_two_frames = []
        for j in range(frame_count+1, min(11,frame_count+3)):
            if '/' in frames[j]:
                next_two_frames.extend(list(map(int, frames[j].split('/'))))
            else:
                next_two_frames.append(int(frames[j]))
        score += sum(next_two_frames)
        frame_count = 11
    return score