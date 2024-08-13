import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    steps = iter(range(max_steps))

    for step in steps:
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
            print(22)  # Bag During CPR
            continue
        
        # Step 2: Apply the examination actions
        examination_order = [3, 4, 5, 6, 7, 8, 25, 27, 16]
        for action in examination_order:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)
                next(steps)  # Consuming a step for the action
                break
        
        # Step 3: Handle unstable tachyarrhythmia
        if any(events[i] > 0 for i in range(29, 38)):  # looking for arrhythmia events
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
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

        print(0)  # DoNothing as a fallback to move to the next step

if __name__ == "__main__":
    stabilize()