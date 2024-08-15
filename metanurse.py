import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action, flush=True)
        actions_taken.add(action)

    def ensure_measurements():
        if 25 not in actions_taken:
            take_action(25)
            return True
        if 26 not in actions_taken:
            take_action(26)
            return True
        if 27 not in actions_taken:
            take_action(27)
            return True
        return False

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

        # Address critical conditions immediately
        if vitals["RR"] is None and any(events[i] > 0 for i in range(7, 14)):
            take_action(4)
            continue

        if vitals["RR"] == 0:
            take_action(29)
            if vitals["HR"] and vitals["HR"] == 0:
                take_action(17)
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        # Airway examination
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)
            if events[6] > 0:
                take_action(32)
            continue

        # Ensure vital sign measurements
        if ensure_measurements():
            continue

        # Maintain minimum MAP level
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        # Circulation/Exposure/Disability if needed
        if any(events[i] > 0 for i in range(7, 21)):
            if any(events[i] > 0 for i in range(14, 21)):
                take_action(5)
            elif any(events[i] > 0 for i in range(21, 28)):
                take_action(6)
            elif any(events[i] > 0 for i in range(28, 33)):
                take_action(7)
            continue

        if step >= 349:
            take_action(48)
            break

        take_action(0)

if __name__ == "__main__":
    stabilize()