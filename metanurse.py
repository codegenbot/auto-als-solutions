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
            return
        if vitals["Sats"] and vitals["Sats"] < 65:
            print(22)  # BagDuringCPR
            return

        # Step 2: Perform ABCDE Examinations
        examinations = [3, 4, 5, 6, 7]  # Airway, Breathing, Circulation, Disability, Exposure
        for action in examinations:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)
                break
        else:
            # Step 3: Evaluate and Treat
            if vitals["MAP"] and vitals["MAP"] < 60:
                print(15)  # GiveFluids
                return
            if vitals["Sats"] and vitals["Sats"] < 88:
                print(30)  # UseNonRebreatherMask
                return
            if vitals["RespRate"] and vitals["RespRate"] < 8:
                print(29)  # UseBagValveMask
                return

            if events[29] > 0 or events[30] > 0:
                print(40)  # DefibrillatorCharge
                return

            # Step 4: Check for Stability
            if all(
                vital is not None and vital >= threshold
                for vital, threshold in zip(
                    [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
                )
            ):
                print(48)  # Finish
                return

        print(0)  # DoNothing

if __name__ == "__main__":
    stabilize()