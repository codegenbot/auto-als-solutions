```
def bowling_score(frames):
    score = 0
    roll_count = [0] * 10
    
    for frame in frames.split('/'):
        if len(frame) > 1:
            rolls = list(map(int, frame))
            roll_count[9 - int(''.join(map(str, rolls)))] += 2
            if rolls[0] == 10 and len(rolls) == 2:
                roll_count[9 - '10'[0]] += 1
        else:
            score += int(frame)
    
    for i in range(9):
        if roll_count[i] > 1:
            score += 20
        elif roll_count[i] == 1:
            score += 10
        if i < 8 and (roll_count[i] > 0 and roll_count[i+1] > 0):
            if roll_count[i] == 2 and int(frames.split('/')[i].split('X')[0]) + 10 == int(frames.split('/')[i+1]):
                score += 30
            elif sum(map(int, frames.split('/')[i].split('-')[:2])) == 10:
                score += 20
    return score