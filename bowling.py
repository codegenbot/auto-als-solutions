def bowling_score(bowling):
    score = 0
    frame = 1
    previous_roll = 0
    for i in range(len(bowling)):
        if bowling[i].isdigit():
            if bowling[i] == "X":
                score += 10 + (10 if frame < 9 and bowling[i + 2].isdigit() else 0)
                frame += 1
            elif bowling[i] == "/":
                first_roll = int(bowling[: i - 1])
                second_roll = 10 - first_roll
                score += first_roll + second_roll
                frame += 1
                if frame < 10:
                    previous_roll = sum(map(int, bowling[i + 1 :].split("/")))
            else:
                first_roll = int(bowling[:i])
                if len(first_roll) == 2:
                    score += 10
                    frame += 1
                elif len(first_roll) > 1 and first_roll[0] != "X":
                    first_roll = int(first_roll)
                    second_roll = 10 - first_roll
                    if previous_roll + first_roll < 10:
                        score += first_roll + second_roll
                    else:
                        score += 10
                    frame += 1
                else:
                    score += 10
                    frame += 1
        return score