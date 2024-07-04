def bowling_score(score_string):
    total_score = 0
    frames = []
    i = 0

    while len(frames) < 10:
        if score_string[i] == "X":
            frames.append([10])
            i += 1
        elif score_string[i + 1] == "/":
            frames.append([int(score_string[i]), 10 - int(score_string[i])])
            i += 2
        else:
            frames.append([int(score_string[i]), int(score_string[i + 1])])
            i += 2

    for frame_index in range(10):
        frame = frames[frame_index]
        total_score += sum(frame)

        if frame[0] == 10:  # Strike
            if frame_index < 9:
                next_two_bowls = frames[frame_index + 1][:2]
                if len(next_two_bowls) < 2:
                    next_two_bowls += frames[frame_index + 2][:1]
                total_score += sum(next_two_bowls)

        elif sum(frame) == 10:  # Spare
            if frame_index < 9:
                total_score += frames[frame_index + 1][0]

    return total_score


# Example usage:
print(bowling_score(input().strip()))