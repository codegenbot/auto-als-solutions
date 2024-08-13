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

        # Step 1: Check for critical conditions
        if vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue
        if vitals["Sats"] and vitals["Sats"] < 65:
            print(22)  # Bag during CPR
            continue

        # Step 2: Apply the examination actions
        examinations = [
            (25, 25), (27, 27), (16, 16), 
            (5, 5), (3, 3), (4, 4), 
            (8, 8), (2, 2)
        ]
        for action, key in examinations:
            if key not in actions_taken:
                actions_taken.add(key)
                print(action)
                break
        else:
            # Step 3: Handle unstable tachyarrhythmia
            if events[29] > 0 or events[30] > 0:
                print(40)  # DefibrillatorCharge
                continue
          
            # Step 4: Check vital parameters and manage states accordingly
            if vitals["MAP"] and vitals["MAP"] < 60:
                print(15)  # GiveFluids
                continue
            if vitals["Sats"] and vitals["Sats"] < 88:
                print(30)  # UseNonRebreatherMask
                continue
            if vitals["RespRate"] and vitals["RespRate"] < 8:
                print(29)  # UseBagValveMask
                continue

            # Step 5: Final stability check
            if all(
                vital is not None and vital >= threshold
                for vital, threshold in zip(
                    [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
                )
            ):
                print(48)  # Finish
                return

if __name__ == "__main__":
    stabilize()