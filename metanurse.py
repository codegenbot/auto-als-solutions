import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    given_fluids = False
    checked_monitor = False

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

        if any(events[i] > 0 for i in range(3, 7)):
            if 3 not in actions_taken:
                take_action(3)
                actions_taken.add(3)
                continue
            if events[7] > 0:
                take_action(29)
                continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 25 not in actions_taken:
                take_action(25)
                actions_taken.add(25)
                continue
            if 30 not in actions_taken:
                take_action(30)
                actions_taken.add(30)
                continue
            take_action(29)
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if not given_fluids:
                take_action(15)
                given_fluids = True
                continue
            if not checked_monitor:
                take_action(16)
                checked_monitor = True
                continue

        if events[21] > 0:
            take_action(6)
            continue
        if events[22] > 0:
            take_action(6)
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        if 1 not in actions_taken:
            take_action(1)
            actions_taken.add(1)
            continue
        if 2 not in actions_taken:
            take_action(2)
            actions_taken.add(2)
            continue
        if 27 not in actions_taken:
            take_action(27)
            actions_taken.add(27)
            continue
        if 25 not in actions_taken:
            take_action(25)
            actions_taken.add(25)
            continue
        if 16 not in actions_taken:
            take_action(16)
            actions_taken.add(16)
            continue
        if 38 not in actions_taken:
            take_action(38)
            actions_taken.add(38)
            continue

        take_action(0)

if __name__ == "__main__":
    stabilize()