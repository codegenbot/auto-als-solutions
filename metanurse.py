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

        if vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            print(22)  # Bag During CPR
            continue

        to_check = [
            (25, "Sats"),
            (27, "MAP"),
            (16, ""),
            (3, "Airway"),
            (4, "Breathing"),
            (5, "Circulation"),
            (8, "Response"),
            (2, "Rhythm")
        ]

        for action, _ in to_check:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)  # Perform the next action in ABCDE steps
                break

        else:  # All examination actions are done, perform treatments
            if vitals["MAP"] and vitals["MAP"] < 60:
                print(15)  # GiveFluids
                continue

            if vitals["Sats"] and vitals["Sats"] < 88:
                print(30)  # UseNonRebreatherMask
                continue

            if vitals["RespRate"] and vitals["RespRate"] < 8:
                print(29)  # UseBagValveMask
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
                
        print(0)  # DoNothing as a default action if no other conditions met

if __name__ == "__main__":
    stabilize()