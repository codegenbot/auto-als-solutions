def bowling_game_score(bowling_game):
    score = 0
    roll = 0
    for i in range(len(bowling_game)):
        if len(bowling_game) > i:
            if bowling_game[i] == 'X':
                score += 10
                if i < 9 and bowling_game[i+1].isdigit() and int(bowling_game[i+1]) != 10:
                    score -= int(bowling_game[i+1])
                roll += 2
            elif bowling_game[i].isdigit():
                first_roll = int(bowling_game[i])
                if i < len(bowling_game) - 1:
                    second_roll = int(bowling_game[i + 1])
                    if second_roll == 10: 
                        score += 10 + (first_roll)
                    else:
                        score += first_roll + second_roll
                    roll += 2
                else:
                    score += first_roll
                    roll += 1
            else:
                first_roll = int(bowling_game[i])
                second_roll = int(bowling_game[i+1])
                score += first_roll + second_roll
                roll += 2
        else:
            break
    return score