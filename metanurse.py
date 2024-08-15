import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    steps = 350

    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:
            take_action(24)  # UseMonitorPads (for synchronized cardioversion)
            continue

        ABCDE_steps = [
            {"action": 3, "conditions": [3, 4, 5, 6]},  # Airway
            {"action": 4, "conditions": [7, 8, 9, 10, 11, 12, 13, 14]},  # Breathing
            {"action": 5, "conditions": [15, 16, 17, 18, 19]},  # Circulation
            {"action": 6, "conditions": [20, 21, 22, 23, 24, 25]},  # Disability
            {"action": 7, "conditions": [26, 27, 28, 29, 30, 31, 32]},  # Exposure
        ]

        for step in ABCDE_steps:
            action = step["action"]
            conditions = step["conditions"]
            if any(events[i] > 0 for i in conditions):
                take_action(action)
                break

        continue

        take_action(48)  # Finish
        break


if __name__ == "__main__":
    stabilize()