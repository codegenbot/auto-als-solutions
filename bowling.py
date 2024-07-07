```
def bowling_score(s):
    score = 0
    frame = 1
    i = 0
    while i < len(s):
        if s[i].isdigit():
            first_roll = int(s[i])
            if i + 1 < len(s) and s[i + 1].isdigit():
                second_roll = int(s[i + 1])
                if first_roll + second_roll == 10:
                    score += 10
                    i += 2
                else:
                    score += first_roll + second_roll
                    i += 2
            elif s[i + 1] == "X":
                score += 10
                i += 2
            else:
                if frame < 9 and (s[i + 1].isdigit() or s[i + 1] == "X"):
                    if first_roll != 10:
                        bonus = 10 - first_roll
                        score += 10
                        i += 2
                    else:
                        score += 10
                        i += 3
                else:
                    break
        else:
            if s[i] == "X":
                score += 10
                i += 1
            elif s[i] == "/":
                score += 5
                i += 2
    return score