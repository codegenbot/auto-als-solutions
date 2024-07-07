```
def bowling_score(s):
    score = 0
    frame = 1
    for i in range(0, len(s), 2):
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
                if s[i] != "/":
                    if frame > 9 and (s[i + 1].isdigit() or s[i + 1] == "X"):
                        break
        else:
            if s[i] == "X":
                score += 10
                frame -= 1
            elif s[i] == "/":
                continue
    return score