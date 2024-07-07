def bowling_score(frames):
    score = 0
    frames = frames.split()
    for i in range(0, len(frames), 2):
        if '/' not in frames[i]:
            score += sum(map(int, frames[i:i+2]))
        elif int(frames[i]) == 10:
            score += 10 + sum(map(int, frames[i+1:i+3]))
        else:
            score += 10 + max(map(int, frames[i:i+2]))
    return score