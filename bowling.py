def bowling_score(frames):
    score = 0
    frames_list = frames.split(' ')
    for i in range(10):
        if '/' in frames_list[i]:
            split_frame = list(map(int, frames_list[i].split('/')))
            if sum(split_frame) == 10:
                score += 10 + sum(split_frame)
            else:
                score += sum(split_frame)
        else:
            score += int(frames_list[i])
    return score

frames = "5/5 3/- 1/2 7/3 5/- 4/- 8/1 0/6 2/- 3/-"
print(bowling_score(frames))