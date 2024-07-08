```
def bowling_score(frames):
    score = 0
    roll_index = 0
    for frame in range(1, 11):
        if frames[roll_index] == "X":
            score += 10 + get_next_two_frames(frames, roll_index)
            roll_index += 3
        elif frames[roll_index] == "/":
            first_roll = int(frames[roll_index - 1])
            second_roll = 10 - int(frames[roll_index + 1][0])
            score += first_roll + second_roll
            roll_index += 2
        else:
            if len(frames) > roll_index + 1 and frames[roll_index] + frames[roll_index + 1] == "10":
                score += 10
                roll_index += 2
            else:
                score += int(frames[roll_index]) + int(frames[roll_index + 1])
                roll_index += 2

    return score


def get_next_two_frames(frames, index):
    score = 0
    for i in range(1, 3):
        if frames[index] == "X":
            score += 10
            break
        else:
            score += int(frames[index])
        index += 1
    return score