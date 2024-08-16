import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    examined_vitals = set()
    exam_steps = [4, 25, 27, 26, 38, 16]

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        if vitals["MAP"] is None or vitals["Sats"] is None or vitals["RR"] is None:
            for action in exam_steps:
                if action not in examined_vitals:
                    take_action(action)
                    examined_vitals.add(action)
                    break
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30 if 30 not in actions_taken else 29)
            actions_taken.add(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in range(3, 7)) and 3 not in actions_taken:
            take_action(3)
            actions_taken.add(3)
            continue

        if any(events[i] > 0 for i in range(7, 15)) and 4 not in actions_taken:
            take_action(4)
            actions_taken.add(4)
            continue

        if any(events[i] > 0 for i in range(15, 20)) and 5 not in actions_taken:
            take_action(5)
            actions_taken.add(5)
            continue

        if any(events[i] > 0 for i in range(20, 26)) and 6 not in actions_taken:
            take_action(6)
            actions_taken.add(6)
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        take_action(48)
        break


if __name__ == "__main__":
    stabilize()