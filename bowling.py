def bowling_score(s):
    score = 0
    frame = 1
    while frame <= 10:
        if s[2 * len(str(frame)) - 3 : 2 * len(str(frame))].isdigit():
            first_roll = int(s[2 * len(str(frame)) - 3 : 2 * len(str(frame))])
            if s[2 * len(str(frame)) : 2 * len(str(frame)) + 1].isdigit():
                second_roll = int(s[2 * len(str(frame)) : 2 * len(str(frame)) + 1])
                if first_roll + second_roll == 10:
                    score += 10
                    frame += 1
                else:
                    score += first_roll + second_roll
                    frame += 1
            elif s[2 * len(str(frame))].upper() == "X":
                if frame < 9 or (
                    frame == 9
                    and sum(
                        int(
                            s[18 - i : i + 3].strip().replace("/", "0").replace("X", 10)
                        )
                    )
                    <= 10
                ):
                    score += 10
                    frame += 1
                else:
                    bonus = 10 - first_roll
                    score += 10 + bonus
                    frame += 1
            elif s[2 * len(str(frame))].upper() == "/":
                if frame < 9 or (
                    frame == 9
                    and sum(
                        int(
                            s[18 - i : i + 3].strip().replace("/", "0").replace("X", 10)
                        )
                    )
                    <= 10
                ):
                    score += first_roll + int(
                        s[2 * len(str(frame)) + 1]
                        .strip()
                        .replace("/", "0")
                        .replace("X", 10)
                    )
                    frame += 1
                else:
                    bonus = 10 - first_roll
                    score += first_roll + bonus
                    frame += 1
        elif s[2 * len(str(frame))].upper() == "X":
            if frame < 9 or (
                frame == 9
                and sum(
                    int(s[18 - i : i + 3].strip().replace("/", "0").replace("X", 10))
                )
                <= 10
            ):
                score += 10
                frame += 1
            else:
                bonus = 10
                score += 10 + bonus
                frame += 1
    return score