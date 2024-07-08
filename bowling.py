```
def bowling_score(frames):
    score = 0
    frame_index = 0
    while frame_index < len(frames):
        if frames[frame_index] == "X":
            score += 30
            frame_index += 1
        elif frames[frame_index] == "/":
            first_roll = int(frames[frame_index - 1])
            second_roll = 10 - int(frames[frame_index + 1][0])
            score += first_roll + second_roll
            frame_index += 2
        else:
            if len(frames) > frame_index + 1 and frames[frame_index] + frames[frame_index + 1] == "10":
                score += 10
                frame_index += 2
                while frame_index < len(frames) and int(frames[frame_index]) != "X" and int(frames[frame_index]) != "/":
                    score += int(frames[frame_index])
                    frame_index += 1
            else:
                first_roll = int(frames[frame_index])
                second_roll = int(frames[frame_index + 1])
                if first_roll + second_roll == 10:
                    score += first_roll + 10
                elif first_roll > 0 and second_roll > 0:
                    score += first_roll + second_roll
                frame_index += 2
    return score