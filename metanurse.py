import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    step = 0

    essential_measurements = [27, 25, 26, 24]

    while step < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        for action in essential_measurements:
            if action not in actions_taken:
                actions_taken.add(action)
                take_action(action)
                step += 1
                break
        else:
            if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
                vitals["MAP"] is not None and vitals["MAP"] < 20
            ):
                take_action(17)
                step += 1
                continue

            if not any(events[i] > 0 for i in range(3, 7)):
                take_action(3)
                step += 1
                continue

            if events[5] > 0:
                take_action(31)
                step += 1
                continue

            if events[6] > 0:
                take_action(32)
                step += 1
                continue

            if not any(events[i] > 0 for i in range(7, 15)):
                take_action(4)
                step += 1
                continue

            if vitals["Sats"] is not None and vitals["Sats"] < 88:
                take_action(30)
                step += 1
                continue

            if vitals["RR"] is not None and vitals["RR"] < 8:
                take_action(29)
                step += 1
                continue

            if not any(events[i] > 0 for i in range(15, 20)):
                take_action(5)
                step += 1
                continue

            if vitals["MAP"] is not None and vitals["MAP"] < 60:
                take_action(15)
                step += 1
                continue

            if vitals["HR"] is not None and vitals["HR"] > 150:
                take_action(11)
                step += 1
                continue

            take_action(48)
            break

        step += 1


if __name__ == "__main__":
    stabilize()