def bowling_game(bowling_score):
    score = 0
    for i in range(0, len(bowling_score), 2):
        if bowling_score[i] == "X":
            score += 30
        elif bowling_score[i].isdigit() and len(str(int(bowling_score[i]))) == 1:
            if (
                bowling_score[i + 1].isdigit()
                and len(str(int(bowling_score[i + 1]))) == 1
            ):
                score += int(bowling_score[i]) + int(bowling_score[i + 1])
            else:
                score += int(bowling_score[i])
        elif bowling_score[i].isdigit() and len(str(int(bowling_score[i]))) > 1:
            score += int(bowling_score[i : i + 2])
    return score