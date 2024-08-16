import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

    def reexamine(event_index, action):
        if any(events[i] > 0 for i in event_index) and action not in examined_vitals:
            take_action(action)
            examined_vitals.add(action)
            return True
        return False

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

        if vitals["MAP"] is None and 27 not in examined_vitals:
            take_action(27)
            examined_vitals.add(27)
            continue

        if vitals["Sats"] is None and 25 not in examined_vitals:
            take_action(25)
            examined_vitals.add(25)
            continue

        if vitals["RR"] is None and 4 not in examined_vitals:
            take_action(4)
            examined_vitals.add(4)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if reexamine(range(3, 7), 3) or reexamine(range(7, 15), 4) or \
           reexamine(range(15, 20), 5) or reexamine(range(20, 26), 6) or \
           reexamine(range(26, 33), 7):
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()