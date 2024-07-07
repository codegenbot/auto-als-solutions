```
def bowling_score(s):
    score = 0
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
                else:
                    score += first_roll + second_roll
            elif s[i] == "X":
                score += 10
                i += 1
            else:
                if s[i] == "/":
                    i += 2
                    continue
        else:
            if s[i] == "X":
                score += 10
                i += 1
            elif s[i] == "/":
                first_roll = 10 - int(s[i-1])
                score += first_roll
                i += 1
            else:
                first_roll, second_roll = map(int, s[i-1:i+1])
                score += first_roll + second_roll
                i += 2
    return score