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

        if vitals["MAP"] and vitals["MAP"] < 20:
            print(17)
            continue
        if vitals["Sats"] and vitals["Sats"] < 65:
            print(22)
            continue
        
        examination_order = [3, 4, 5, 6, 7, 8, 25, 27, 16]
        for action in examination_order:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)
                next(steps)
                break
        
        if any(events[i] > 0 for i in range(29, 38)):
            print(40)
            continue
        
        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)
            continue
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60]
            )
        ):
            print(48)
            return

        print(0)

if __name__ == "__main__":
    stabilize()