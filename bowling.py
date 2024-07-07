```
def bowling_score(s):
    score = 0
    frame = 1
    while frame <= 10:
        if s[2*len(str(frame))-2].isdigit():
            first_roll = int(s[2*len(str(frame))-2])
            second_roll = int(s[2*len(str(frame))-1]) if len(str(frame)) == 2 else 0
            if first_roll + second_roll == 10:
                score += 10
                frame += 1
            elif second_roll > 0 and (first_roll + second_roll) > 10:
                score += 10 - first_roll
                frame += 1
            else:
                score += first_roll + second_roll
                frame += 1
        elif s[2*len(str(frame))-2] == "X":
            if len(str(frame)) == 1:
                score += 10
                frame += 1
            else:
                if s[4*len(str(frame))-3].isdigit():
                    second_roll = int(s[4*len(str(frame))-3]) + int(s[4*len(str(frame))-2])
                    score += 10 + second_roll
                elif s[4*len(str(frame))-3] == "X":
                    score += 15
                else:
                    score += 10 + 10 - int(s[4*len(str(frame))-3])
                frame += 1
        else:
            if len(str(frame)) == 1:
                score += 10
                frame += 1
            else:
                if s[2*len(str(frame))-1] == "/":
                    first_roll = int(s[2*len(str(frame))-2]) + 10 - int(s[4*len(str(frame))-3])
                    score += first_roll
                    frame += 1
                else:
                    second_roll = int(s[4*len(str(frame))-2]) + int(s[4*len(str(frame))-1])
                    if first_roll + second_roll > 10:
                        score += 10 + (second_roll - 10)
                    else:
                        score += first_roll + second_roll
                    frame += 1
    return score