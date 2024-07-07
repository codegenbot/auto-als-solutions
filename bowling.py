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
                    frame -= 1
                else:
                    score += first_roll + second_roll
            elif s[i + 1] == "X":
                score += 10
                frame -= 1
            else:
                if i + 2 < len(s) and s[i + 2].isdigit():
                    third_roll = int(s[i + 2])
                    score += first_roll + second_roll + third_roll
                    frame -= 1
                else:
                    break
        elif s[i] == "X":
            score += 10
            frame -= 1
        i += 1
    return score