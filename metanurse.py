import sys


def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    def need_examination(category):
        exam_actions = {
            "A": [3],
            "B": [25, 5, 16],
            "C": [27, 16],
        }
        return any(action not in actions_taken for action in exam_actions[category])

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    [
                        "HeartRate",
                        "RespRate",
                        "CapillaryGlucose",
                        "Temperature",
                        "MAP",
                        "Sats",
                        "Resps",
                    ],
                    vital_signs_values,
                )
            )
        }

        if need_examination("A"):
            take_action(3)
            continue

        if need_examination("B"):
            if 25 not in actions_taken:
                take_action(25)
                continue
            take_action(16)
            continue

        if need_examination("C"):
            if 27 not in actions_taken:
                take_action(27)
                continue
            take_action(16)
            continue

        unstable_tachyarrhythmia = (
            events[29] > 0 or events[30] > 0 or events[31] > 0 or events[32] > 0
        )
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        take_action(48)


if __name__ == "__main__":
    stabilize()