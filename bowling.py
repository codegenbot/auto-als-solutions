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
                if s[i].isdigit():
                    third_roll = int(s[i])
                    i += 1
                    if first_roll + second_roll + third_roll == 15:
                        score += 10
                    else:
                        score += first_roll + second_roll + third_roll
                elif s[i] == "X":
                    score += 10
                    frame -= 1
                    i += 1
        elif s[i] == "X":
            if frame < 9:
                score += 10
                frame -= 1
            else:
                while i < len(s) and s[i].isdigit():
                    third_roll = int(s[i])
                    i += 1
                score += 10 + third_roll
        elif s[i] == "/":
            if frame < 9:
                score += 5
                frame -= 1
            else:
                while i < len(s) and s[i].isdigit():
                    third_roll = int(s[i])
                    i += 1
                score += 5 + third_roll
    return score