import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

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

        if vitals["Sats"] is None:
            take_action(25)  # UseSatsProbe
            continue
        elif vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is None:
            take_action(4)  # ExamineBreathing
            continue
        elif vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is None:
            take_action(27)  # UseBloodPressureCuff
            continue
        elif vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["HR"] is None:
            take_action(5)  # ExamineCirculation
            continue
        elif vitals["HR"] > 150:
            take_action(24)  # UseMonitorPads (for synchronized cardioversion)
            continue

        ABCDE_steps = [
            {"action": 3, "conditions": [3, 4, 5, 6]},  # Airway
            {"action": 4, "conditions": [7, 8, 9, 10, 11, 12, 13, 14]},  # Breathing
            {"action": 5, "conditions": [15, 16, 17, 18, 19]},  # Circulation
            {"action": 6, "conditions": [20, 21, 22, 23, 24]},  # Disability
            {"action": 7, "conditions": [25, 26, 27, 28, 29, 30, 31, 32]},  # Exposure
        ]

        action_taken = False
        for step in ABCDE_steps:
            action = step["action"]
            conditions = step["conditions"]
            if any(events[i] > 0 for i in conditions):
                take_action(action)
                action_taken = True
                break

        if not action_taken:
            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()