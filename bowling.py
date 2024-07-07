```
def bowling_score(s):
    score = 0
    frame = 1
    i = 0
    while i < len(s):
        if s[i].isdigit():
            first_roll = int(s[i])
            i += 1
            if i < len(s) and s[i].isdigit():
                second_roll = int(s[i])
                i += 1
                if first_roll + second_roll == 10:
                    score += 10
                    frame -= 1
                else:
                    score += first_roll + second_roll
            elif s[i] == "X":
                score += 10
                frame -= 1
                i += 1
            else:
                if frame > 9 and (s[i].isdigit() or s[i] == "X"):
                    break
        else:
            if s[i] == "X":
                score += 10
                frame -= 1
                i += 1
            elif s[i] == "/":
                score += 10 - int(s[i-1])
                i += 1
    return score