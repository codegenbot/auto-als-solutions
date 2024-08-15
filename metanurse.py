import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    mandatory_actions = [27, 25, 38, 25]
    examine_order = [3, 4, 5, 6, 7, 8]

    for step in range(350):
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:
            take_action(24)
            continue

        for action in mandatory_actions:
            if action not in actions_taken:
                actions_taken.add(action)
                take_action(action)
                break
        else:
            for exam in examine_order:
                if exam not in actions_taken:
                    actions_taken.add(exam)
                    take_action(exam)
                    break

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            continue

        if events[5] > 0:
            take_action(31)
            continue
        if events[6] > 0:
            take_action(32)
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue
        if events[7] > 0:
            take_action(29)
            continue
        if events[14] > 0:
            take_action(19)
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue

        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        take_action(0)

if __name__ == "__main__":
    stabilize()