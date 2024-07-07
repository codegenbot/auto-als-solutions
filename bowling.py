```
def bowling_score(s):
    score = 0
    i = 0
    while i < len(s):
        if s[i].isdigit():
            first_roll = int(s[i])
            if i + 1 < len(s) and s[i + 1].isdigit():
                second_roll = int(s[i + 1])
                if first_roll + second_roll == 10:
                    score += 10
                    i += 1
                else:
                    score += first_roll + second_roll
                    i += 2
            elif s[i] == "X":
                score += 10
                i += 1
            elif s[i] == "/":
                score += 5
                i += 2
        elif s[i] == "X" and i + 1 < len(s) and s[i+1].isdigit():
            score += 10 + int(s[i + 1])
            i += 2
        i += 1
    return score