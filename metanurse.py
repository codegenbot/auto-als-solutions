import sys

def stabilize():
    max_steps = 350
    actions_needed = [25, 27, 16, 3, 4, 5, 6, 7]
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

        # Taking needed actions in sequence
        if actions_needed:
            action = actions_needed.pop(0)
            actions_taken.add(action)
            print(action)
            continue

        # Treating based on measurements
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # Use Non-Rebreather Mask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # Use Bag Valve Mask
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # Start Chest Compression
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # Give Fluids
            continue

        unstable_tachyarrhythmia = events[29] > 0 or events[30] > 0 or events[31] > 0
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                actions_taken.add(28)
                print(28)  # Attach Defib Pads
                continue
            print(41)  # Increase Defibrillator Current
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
    
        print(48)  # In case all conditions met
        return

if __name__ == "__main__":
    stabilize()