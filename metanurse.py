import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    actions = [25, 27, 16, 5, 3, 4, 8]  # Ordered actions to examine patient

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

        if actions:
            print(actions.pop(0))
            continue

        if events[29] > 0:  # HeartRhythmSVT
            print(9)  # Give Adenosine
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(22)  # Bag During CPR
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # Give Fluids
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # Use Non-Rebreather Mask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # Use Bag-Valve Mask
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

        print(1)  # Redundant: Perform a check for signs of life

if __name__ == "__main__":
    stabilize()