import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()

    def get_measurements():
        if 25 not in actions_taken:
            return 25
        if 26 not in actions_taken:
            return 26
        if 27 not in actions_taken:
            return 27
        if 28 not in actions_taken:
            return 28
        return None

    for step in range(max_steps):
        observations = list(map(float, sys.stdin.readline().strip().split()))
        if len(observations) != 53:
            continue

        events, vitals_times, vitals_values = observations[:33], observations[33:40], observations[40:]
        vitals = {
            "HR": vitals_values[0] if vitals_times[0] > 0 else None,
            "RR": vitals_values[1] if vitals_times[1] > 0 else None,
            "MAP": vitals_values[4] if vitals_times[4] > 0 else None,
            "Sats": vitals_values[5] if vitals_times[5] > 0 else None,
        }

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)
            if events[6] > 0:
                take_action(32)
            continue

        measurement_action = get_measurements()
        if measurement_action:
            take_action(measurement_action)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20 or vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in range(7, 14)):
            take_action(4)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if any(events[i] > 0 for i in range(14, 21)):
            take_action(5)
            continue

        if step >= 349:
            take_action(48)
            break

        take_action(0)

if __name__ == "__main__":
    stabilize()