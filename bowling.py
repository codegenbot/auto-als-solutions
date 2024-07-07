```
def bowling_score(s):
    score = 0
    frame = 1
    while s:
        if s[:2] == "X ":
            score += 10
            s = s[2:]
            if len(s) >= 2 and (s[:2] in ["11", "20"] or s[:2].isdigit()):
                score += int(s[:2])
                s = s[2:]
        elif s[:1] == "X":
            score += 10
            s = s[1:]
            if len(s) >= 1 and (s[:1].isdigit() or s[:2] in ["11", "20"]):
                if int(s[:1]) + 10 <= 10:
                    score += int(s[:1]) + 10
                    s = s[1:]
                else:
                    score += 10
                    s = s[1:]
        elif s[:2].isdigit() and int(s[:2]) < 10:
            if int(s[:2]) + int(s[1:2]) == 10:
                score += 10
                s = s[2:]
            else:
                score += int(s[:2]) + int(s[1:])
                s = s[2:]
        elif s[:2].isdigit() and int(s[:2]) == 10:
            score += 10
            s = s[2:]
        elif s[:1] == "/":
            if len(s) >= 3 and (s[:2].isdigit() or s[:2] in ["11", "20"]):
                if int(s[:1]) + int(s[1:2]) <= 10:
                    score += int(s[:1]) + int(s[1:])
                    s = s[2:]
                else:
                    score += 10
                    s = s[2:]
            elif len(s) >= 2 and (s[:2].isdigit() or s[:2] in ["11", "20"]):
                if int(s[:2]) <= 10:
                    score += int(s[:2])
                    s = s[2:]
                else:
                    score += 10
                    s = s[2:]
        elif s[:1].isdigit():
            score += int(s[:1])
            s = s[1:]
    return score