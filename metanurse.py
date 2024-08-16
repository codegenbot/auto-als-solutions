import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    examined_vitals = set()
    has_viewed_monitor = False

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

        if not has_viewed_monitor:
            take_action(16)
            has_viewed_monitor = True
            continue

        if 3 not in actions_taken:
            take_action(3)
            actions_taken.add(3)
            continue

        if 4 not in actions_taken:
            take_action(4)
            actions_taken.add(4)
            continue

        if 5 not in actions_taken:
            take_action(5)
            actions_taken.add(5)
            continue

        if 6 not in actions_taken:
            take_action(6)
            actions_taken.add(6)
            continue

        if 7 not in actions_taken:
            take_action(7)
            actions_taken.add(7)
            continue
                
        if vitals["MAP"] is None:
            if 27 not in examined_vitals:
                take_action(27)
                examined_vitals.add(27)
                continue

        if vitals["Sats"] is None:
            if 25 not in examined_vitals:
                take_action(25)
                examined_vitals.add(25)
                continue

        if vitals["RR"] is None:
            take_action(4)
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

        if any(events[i] > 0 for i in range(26, 33)) or vitals["HR"] is not None and (vitals["HR"] < 60 or vitals["HR"] > 100):
            take_action(2)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()