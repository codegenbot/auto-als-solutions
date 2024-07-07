```python
def bowling_score(frames):
    score = 0
    for i in range(10):
        if '/' in frames[i]:
            split_frame = list(map(int, frames[i].split('/')))
            score += sum(split_frame)
            if sum(split_frame) == 10:
                next_frame = int(frames[i+1]) if i < 9 else 0
                score += next_frame
        else:
            score += int(frames[i])
    return score