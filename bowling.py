def bowling_score(frames):
    score = 0
    frame_scores = frames.split()
    for i in range(0, len(frame_scores), 2):
        if frame_scores[i] == '10':
            score += 10
        else:
            score += int(frame_scores[i]) + int(frame_scores[i+1])
    return score