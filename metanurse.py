import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

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

        if 25 not in actions_taken:
            actions_taken.add(25)
            print(25)  # UseSatsProbe
            continue

        if 27 not in actions_taken:
            actions_taken.add(27)
            print(27)  # UseBloodPressureCuff
            continue

        if 16 not in actions_taken:
            actions_taken.add(16)
            print(16)  # ViewMonitor
            continue
        
        # Immediate Checks
        if vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # Start Chest Compression
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 65:
            print(22)  # Bag During CPR
            continue
        
        # Evaluate Actions based on priority
        unstable_tachyarrhythmia = events[29] > 0 or events[30] > 0 or events[32] > 0

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # Give Fluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # Use Non Rebreather Mask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # Use Bag Valve Mask
            continue

        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                actions_taken.add(28)
                print(28)  # Attach Defib Pads
            elif 40 not in actions_taken:
                actions_taken.add(40)
                print(40)  # Charge Defib
            else:
                print(41)  # Increase Defib Current
            continue
        
        # Continue ABCDE Assessments if essential actions are taken 
        if 3 not in actions_taken:
            actions_taken.add(3)
            print(3)  # Examine Airway
            continue

        if 4 not in actions_taken:
            actions_taken.add(4)
            print(4)  # Examine Breathing
            continue

        if 5 not in actions_taken:
            actions_taken.add(5)
            print(5)  # Examine Circulation
            continue
        
        if 8 not in actions_taken:
            actions_taken.add(8)
            print(8)  # Examine Response
            continue

        # Verify Stabilization
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return
        
        # Default to Do Nothing to wait for further inputs if necessary
        print(0)  # Do Nothing

if __name__ == "__main__":
    stabilize()