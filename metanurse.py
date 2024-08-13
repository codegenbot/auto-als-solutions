import sys

def stabilize():
    max_steps = 350
    actions_taken = {action: False for action in [25, 27, 16, 5, 3, 4, 8, 2]}

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

        for action, taken in actions_taken.items():
            if not taken:
                actions_taken[action] = True
                print(action)
                break
        else:
            if vitals.get("MAP") and vitals["MAP"] < 20:
                print(17)
                continue
            if vitals.get("Sats") and vitals["Sats"] < 65:
                print(22)
                continue
            if any(events[i] > 0 for i in range(29, 37)):
                print(9)
                continue
            if vitals.get("MAP") and vitals["MAP"] < 60:
                print(15)
                continue
            if vitals.get("Sats") and vitals["Sats"] < 88:
                print(30)
                continue
            if vitals.get("RespRate") and vitals["RespRate"] < 8:
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

            print(48)
            return

if __name__ == "__main__":
    stabilize()