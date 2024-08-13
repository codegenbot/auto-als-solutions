import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
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
                    "Resps"
                ]
            )
        }

        # Measure vitals if necessary
        if 25 not in actions_taken:
            actions_taken.add(25)
            print(25)
            continue

        if 27 not in actions_taken:
            actions_taken.add(27)
            print(27)
            continue

        if 16 not in actions_taken:
            actions_taken.add(16)
            print(16)
            continue

        # Assess airway, breathing, circulation, disability, exposure
        if 3 not in actions_taken:
            actions_taken.add(3)
            print(3)
            continue

        if 4 not in actions_taken:
            actions_taken.add(4)
            print(4)
            continue

        if 5 not in actions_taken:
            actions_taken.add(5)
            print(5)
            continue

        if 8 not in actions_taken:
            actions_taken.add(8)
            print(8)
            continue
        
        # Stabilization steps
        if vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # Start chest compressions
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            print(22)  # Bag during CPR
            continue
        
        unstable_tachyarrhythmia = events[29] > 0 or events[30] > 0 or events[31] > 0
        
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                actions_taken.add(28)
                print(28)  # Attach defib pads
                continue
            if 40 not in actions_taken:
                actions_taken.add(40)
                print(40)  # Defibrillator charge
                continue
            print(41)  # Defibrillator current up
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # Give fluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # Use non-rebreather mask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # Use bag-valve mask
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

        print(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()