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

        # ABCD Examination stage
        if 3 not in actions_taken:
            take_action(3)
            continue
        if 4 not in actions_taken:
            take_action(4)
            continue
        if 5 not in actions_taken:
            take_action(5)
            continue
        if 6 not in actions_taken:
            take_action(6)
            continue
        if 7 not in actions_taken:
            take_action(7)
            continue

        # Initial Assessments and Attachments
        if 25 not in actions_taken:
            take_action(25)
            continue
        if 27 not in actions_taken:
            take_action(27)
            continue
        if 16 not in actions_taken:
            take_action(16)
            continue

        # Check Vital Signs
        if (
            vitals["MAP"] is None
            or vitals["RespRate"] is None
            or vitals["Sats"] is None
        ):
            if vitals["MAP"] is None and 38 not in actions_taken:
                take_action(38)
                continue
            if vitals["RespRate"] is None and 4 not in actions_taken:
                take_action(4)
                continue
            if vitals["Sats"] is None and 16 not in actions_taken:
                take_action(16)
                continue

        # Immediate Intervention based on critical values
        if vitals["MAP"] and vitals["MAP"] < 20:
            take_action(17)
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            take_action(22)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            take_action(29)
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            take_action(48)
            return

        take_action(48)
        return


if __name__ == "__main__":
    stabilize()