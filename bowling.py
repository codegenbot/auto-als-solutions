```
def bowling_score(frames):
    score = 0
    frames = [int(x) for x in frames.replace('/', '')]
    for i in range(0, len(frames), 2):
        if sum(frames[i:i+2]) == 10:
            if i < len(frames) - 1 and frames[i+2] > 0:
                score += 10 + sum(frames[i+2:])
            else:
                score += sum(frames[i:i+2])
        elif frames[i] == 10:
            score += 10
            score += sum(frames[i+1:])
        else:
            score += sum(frames[i:i+2])
    return score

frames = "7/3/5/5/10/0/1/7/6/4"
print(bowling_score(frames))