import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if times[1] == 0 and 25 not in actions_taken:
            take_action(25)
            actions_taken.add(25)
            continue
        if times[4] == 0 and 27 not in actions_taken:
            take_action(27)
            actions_taken.add(27)
            continue
        if (vitals["MAP"] is None or vitals["Sats"] is None) and 16 not in actions_taken:
            take_action(16)
            actions_taken.add(16)
            continue

        if any(events[i] > 0 for i in range(3, 7)) and 3 not in actions_taken:
            take_action(3)
            actions_taken.add(3)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 30 not in actions_taken:
                take_action(30)
                continue
        elif vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if times[1] == 0 and 25 not in actions_taken:
            take_action(25)
            actions_taken.add(25)
            continue
        if times[2] == 0 and 16 not in actions_taken:
            take_action(16)
            actions_taken.add(16)
            continue
        if not any(events[i] > 0 for i in range(7, 15)) and 4 not in actions_taken:
            take_action(4)
            actions_taken.add(4)
            continue
        if not any(events[i] > 0 for i in range(15, 20)) and 5 not in actions_taken:
            take_action(5)
            actions_taken.add(5)
            continue
        if not any(events[i] > 0 for i in range(20, 26)) and 6 not in actions_taken:
            take_action(6)
            actions_taken.add(6)
            continue
        if not any(events[i] > 0 for i in range(26, 33)) and 7 not in actions_taken:
            take_action(7)
            actions_taken.add(7)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()