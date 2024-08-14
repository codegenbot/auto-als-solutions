import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        actions_taken.add(action)
        print(action)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values,
                vital_signs_times,
                [
                    "HeartRate",
                    "RespRate",
                    "CapillaryGlucose",
                    "Temperature",
                    "MAP",
                    "Sats",
                    "Resps",
                ],
            )
        }

        # Immediate critical actions
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
            continue
        
        # Address unstable tachyarrhythmia
        if any(events[i] > 0 for i in [29, 30, 31]):
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)
            continue

        # Check vitals immediately if not already done
        if 25 not in actions_taken:
            take_action(25)
            continue
        if 27 not in actions_taken:
            take_action(27)
            continue
        if 16 not in actions_taken:
            take_action(16)
            continue

        # Examine ABCDE systematically
        if 3 not in actions_taken:  # Airway
            take_action(3)
            continue
        if 4 not in actions_taken:  # Breathing
            take_action(4)
            continue
        if 5 not in actions_taken:  # Circulation
            take_action(5)
            continue
        if 6 not in actions_taken:  # Disability
            take_action(6)
            continue
        if 7 not in actions_taken:  # Exposure
            take_action(7)
            continue

        # Address hypotension
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        # Address low oxygen saturation
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        # Address low respiratory rate
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        # Check for stabilization
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            take_action(48)
            return

    # End after max steps
    take_action(48)

if __name__ == "__main__":
    stabilize()