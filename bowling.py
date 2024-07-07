```
def bowling_score(s):
    score = 0
    frame = 1
    for i in range(0, len(s), 2):
        if s[i].isdigit():
            strike = False
            if i < len(s) - 1 and s[i+1] == 'X':
                strike = True
            else:
                first = int(s[i])
                second = int(s[i+1]) if s[i+1].isdigit() else 10
                score += first + second
                if strike:
                    score += first + second
                    frame += 2
                else:
                    if first + second == 10:
                        frame += 1
                    else:
                        frame += 1
        else:
            score += 10
            frame += 1
    return score