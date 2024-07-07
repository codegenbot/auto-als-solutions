```
def bowling_score(s):
    score = 0
    i = 0
    while i < len(s):
        if s[i].isdigit():
            first_roll = int(s[i])
            if i + 1 < len(s) and s[i+1].isdigit():
                second_roll = int(s[i+1])
                if first_roll + second_roll == 10:
                    score += 10
                    i += 2
                else:
                    score += first_roll + second_roll
                    i += 2
            elif s[i+1] == "X":
                score += 10
                i += 2
            else:
                if s[i+1].isdigit():
                    second_roll = int(s[i+1])
                    if first_roll + second_roll == 10:
                        score += 10
                        i += 2
                    else:
                        score += first_roll + second_roll
                        i += 2
                elif s[i+1] == "X":
                    score += 10
                    i += 1
                else:
                    if first_roll == 10:
                        bonus = int(s[i+2])
                        score += 10 + bonus
                        i += 3
                    else:
                        i += 2
        elif s[i] == "X":
            if i != len(s) - 1 and s[i+1].isdigit():
                second_roll = int(s[i+1])
                score += 10 + second_roll
                i += 2
            else:
                score += 10
                i += 1
        elif s[i] == "/":
            if i != len(s) - 1 and s[i+1].isdigit():
                second_roll = int(s[i+1])
                first_roll = 10 - second_roll
                score += first_roll + second_roll
                i += 2
            else:
                i += 1
    return score