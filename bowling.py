Here is the solution:

def bowling_score(rolls):
    score = 0
    roll = 0
    for frame in range(10):
        if rolls[roll] == 'X':
            score += 30
            roll += 2
        elif '/' in rolls[roll:roll+2]:
            first, second = map(int, rolls[roll:].split('/')[:2])
            score += first + second
            roll += 3
        else:
            first, second = map(int, rolls[roll:].split()[:2])
            score += first + second
            roll += 2
    return score