import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    # Priority actions
    initial_checks = [27, 25, 38, 16]
    examine_order = [3, 4, 5, 6, 7, 8]
    actions_taken = set()
    critical_vitals = ('Sats', 'MAP', 'RR')

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

        # Immediate critical actions
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        if vitals["HR"] and vitals["HR"] > 150:
            take_action(24)
            continue

        actions_orders = [
            (vitals["Sats"], 88, 30),
            (vitals["RR"], 8, 29),
            (vitals["MAP"], 60, 15),
        ]
        for vital, threshold, action in actions_orders:
            if vital is not None and vital < threshold:
                take_action(action)
                continue

        # Perform initial checks
        for check in initial_checks:
            if check not in actions_taken:
                actions_taken.add(check)
                take_action(check)
                break
        else:
            # Examine in order
            for exam in examine_order:
                if exam not in actions_taken:
                    actions_taken.add(exam)
                    take_action(exam)
                    break

        # Handle specific events
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

    # Finish the scenario if 350 steps are reached
    take_action(48)

if __name__ == "__main__":
    stabilize()