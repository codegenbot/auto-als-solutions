```

    def bowling_game_score(bowling_game):
        score = 0
        roll = 0
        for frame in range(1, 11):
            if len(bowling_game) > roll:
                if bowling_game[roll] == 'X':
                    score += 10 + (10 - int(bowling_game[roll+1])) if roll < 9 and bowling_game[roll+2] != 'X' else 10
                    roll += 2
                elif bowling_game[roll].isdigit():
                    first_roll = int(bowling_game[roll])
                    if len(bowling_game) > roll + 1:
                        second_roll = int(bowling_game[roll + 1])
                        if second_roll == 10: 
                            score += 10 + (first_roll + 10)
                        else:
                            score += first_roll + second_roll
                        roll += 2
                    else:
                        score += first_roll
                        roll += 1
                else:
                    first_roll = int(bowling_game[roll])
                    second_roll = int(bowling_game[roll+1])
                    score += first_roll + second_roll
                    roll += 2
            else:
                break
        return score