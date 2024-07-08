```
def bowling_score(frames):
    score = 0
    frames = frames.split('/')
    for frame in frames:
        if len(frame) == 1:
            score += 10
        elif len(frame) == 2:
            first_roll = int(frame[0])
            second_roll = int(frame[1])
            if first_roll + second_roll == 10:
                score += 10
            else:
                score += first_roll + second_roll
        elif len(frame.replace('-', '').replace('/', '')) > 2:
            if 'X' in frame or str(sum([int(x) for x in frame.replace('-', '').replace('/', '')])) + '/' in frame:
                if 'X' in frame:
                    score += 10
                else:
                    first_roll = int(str(sum([int(x) for x in frame.replace('-', '').replace('/', '')]))) 
                    second_roll = int(frame[3]) 
                    third_roll = int(frame[4])
                    score += first_roll + second_roll + third_roll
            else:
                rolls = [int(x) for x in frame.replace('-', '').replace('/', '')]
                score += sum(rolls)
    return score

frames = "7/3/5/5/10/0/1/7/6/4"
print(bowling_score(frames))