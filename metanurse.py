import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    critical_checks = [25, 27, 38, 16]  # Attach Sats probe, BP cuff, Take BP, View Monitor
    actions_taken = set()
    steps = 0

    def need_more_vitals(vitals):
        return not all(vitals.values())

    while steps < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            steps += 1
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] else None,
            "RR": values[1] if times[1] else None,
            "MAP": values[4] if times[4] else None,
            "Sats": values[5] if times[5] else None,
        }

        if need_more_vitals(vitals):
            for check in critical_checks:
                if check not in actions_taken:
                    actions_taken.add(check)
                    take_action(check)
                    steps += 1
                    break
            continue

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            steps += 1
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            steps += 1
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            steps += 1
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            steps += 1
            continue

        if any(events[i] > 0 for i in [3, 4, 5, 6]): # Airway
            take_action(3)
            steps += 1
            continue

        if any(events[i] > 0 for i in [7, 8, 9, 10, 11, 12, 13, 14]): # Breathing
            take_action(4)
            steps += 1
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:
            take_action(24)
            steps += 1
            continue

        if any(events[i] > 0 for i in [15, 16, 17, 18, 19]): # Circulation
            take_action(5)
            steps += 1
            continue

        if any(events[i] > 0 for i in [20, 21, 22, 23, 24, 25]): # Disability
            take_action(6)
            steps += 1
            continue

        if any(events[i] > 0 for i in [26, 27, 28, 29, 30, 31, 32]): # Exposure
            take_action(7)
            steps += 1
            continue

        take_action(0)
        steps += 1

    take_action(48)

if __name__ == "__main__":
    stabilize()