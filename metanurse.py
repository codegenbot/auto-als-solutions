import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    critical_checks = [27, 25, 38, 16]
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
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

        for check in critical_checks:
            if check not in actions_taken:
                actions_taken.add(check)
                take_action(check)
                break
        else:
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

            if vitals["HR"] is not None and vitals["HR"] > 150:
                take_action(24)
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

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()