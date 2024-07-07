def bowling_score(game):
    score = 0
    frames = game.split("/")
    for i in range(len(frames)):
        if frames[i] == "X":
            score += 30
        elif len(frames[i]) == 1:
            score += int(frames[i])
        else:
            frame_value = int(frames[i][0])
            score += frame_value + (10 - int(frames[i][1]))
    return score