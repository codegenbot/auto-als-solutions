import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def examine_abcde():
        for action in [3, 4, 5, 6, 7]:
            if action not in actions_taken:
                actions_taken.add(action)
                take_action(action)
                return True
        return False

    def ensure_vitals():
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(17)
            return True
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            return True
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            actions_taken.add(25)
            take_action(30)
            return True
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            return True
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            actions_taken.add(27)
            take_action(15)
            return True
        return False

    def handle_rhythm():
        if any(events[i] > 0 for i in range(28, 38)):
            take_action(28)
            return True
        return False

    def measure_vitals():
        if 27 not in actions_taken:
            actions_taken.add(27)
            take_action(27)
            return True
        if 25 not in actions_taken:
            actions_taken.add(25)
            take_action(25)
            return True
        if 16 not in actions_taken:
            actions_taken.add(16)
            take_action(16)
            return True
        if 38 not in actions_taken:
            actions_taken.add(38)
            take_action(38)
            return True
        return False

    actions_taken = set()
    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {"HR": values[0] if times[0] > 0 else None, "RR": values[1] if times[1] > 0 else None,
                  "MAP": values[4] if times[4] > 0 else None, "Sats": values[5] if times[5] > 0 else None}

        if ensure_vitals():
            continue
        if not examine_abcde():
            if handle_rhythm() or measure_vitals():
                continue
            take_action(48)
            break

if __name__ == "__main__":
    stabilize()