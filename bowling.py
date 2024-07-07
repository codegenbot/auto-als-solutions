```
def bowling_score(s):
    score = 0
    i = 0
    while i < len(s):
        if s[i] == "X":
            score += 10
            i += 1
            if i < len(s) and s[i] in "12345678":
                first_roll = int(s[i])
                if i + 1 < len(s) and s[i + 1].isdigit():
                    second_roll = int(s[i + 1])
                    if first_roll + second_roll == 10:
                        score += 10
                    else:
                        score += first_roll + second_roll
                elif s[i + 1] == "X":
                    score += 10
            i += 1
        elif s[i].isdigit() and (i + 1 < len(s) and s[i + 1].isdigit()):
            first_roll = int(s[i])
            second_roll = int(s[i + 1])
            if first_roll + second_roll == 10:
                score += 10
            else:
                score += first_roll + second_roll
            i += 2
        elif s[i] == "/":
            first_roll = int(s[i - 1])
            second_roll = int(s[i + 1])
            score += first_roll + second_roll
            i += 2
        else:
            if s[i].isdigit():
                score += int(s[i])
            i += 1
    return score