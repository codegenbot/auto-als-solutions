import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing if incorrect input length
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        # Vital signs with measurements only if timing > 0
        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        # Respond to cardiac arrest scenario
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        # Check and stabilize vital signs
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Perform initial critical checks
        initial_checks = [
            27,
            25,
            38,
            16,
        ]  # BP cuff, Sats probe, BP measure, ViewMonitor
        for check in initial_checks:
            if check not in actions_taken:
                actions_taken.add(check)
                take_action(check)
                break
        else:
            # ABCDE Assessment sequence
            for indices, action in [
                (range(3, 7), 3),  # Airway events
                (range(7, 15), 4),  # Breathing events
                (range(15, 20), 5),  # Circulation events
                (range(20, 26), 6),  # Disability events
                (range(26, 33), 7),  # Exposure events
            ]:
                if any(events[i] > 0 for i in indices):
                    take_action(action)
                    break
            else:
                take_action(48)  # Finish assessment
                break


if __name__ == "__main__":
    stabilize()