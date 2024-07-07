```
def bowling_score(s):
    score = 0
    frame = 1
    for i in range(0, len(s), 2):
        first_roll = int(s[i]) if s[i].isdigit() else (10 if s[i] == "X" else 10 / 2)
        if i + 1 < len(s) and s[i+1].isdigit():
            second_roll = int(s[i+1])
            score += first_roll + second_roll
            if frame < 9:
                if first_roll + second_roll == 10:
                    frame -= 1
                elif first_roll != 10:
                    frame -= 0.5
        else:
            score += first_roll
            if s[i] == "X":
                frame -= 1
            elif s[i] == "/":
                continue
    return int(score)