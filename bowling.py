```
def bowling_score(frames):
    score = 0
    frame = 1
    i = 0
    while i < len(frames):
        if frames[i] == "X":
            if frame == 10:
                score += 10 + int(frames[i-2])
            else:
                score += 10 + int(frames[i-1])
            i += 1
        elif frames[i] == "/":
            score += 10
            i += 2
        else:
            first_roll = int(frames[i])
            if frame < 10 and frames[i+1].isdigit():
                second_roll = int(frames[i+1])
                if first_roll + second_roll == 10:
                    score += 10
                    i += 2
                else:
                    score += first_roll + second_roll
                    i += 2
            elif frame < 10 and not frames[i+1].isdigit():
                score += first_roll + int(frames[i+1])
                i += 2
            else:
                if frame < 9:
                    score += first_roll
                    i += 1
                elif frame == 9 and frames[i] != "X":
                    score += first_roll + int(frames[i+1])
                    i += 2
                else:
                    score += first_roll + 10
                    i += 1
        frame += 1
    return score