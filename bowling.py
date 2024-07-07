def bowling_score(frames):
    score = 0
    for i in range(10):
        if "/" in frames[i * 2 : i * 2 + 1]:
            parts = frames[i * 2 : i * 2 + 1].split("/")
            score += int(parts[0]) + int(parts[1])
        else:
            score += int(frames[i * 2 : i * 2 + 1])
    return score