import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values, vital_signs_times,
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                 "MAP", "Sats", "Resps"]
            )
        }

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
        if 6 not in actions_taken:
            actions_taken.add(6)
            print(6)
            continue
        if 7 not in actions_taken:
            actions_taken.add(7)
            print(7)
            continue
        if 2 not in actions_taken:
            actions_taken.add(2)
            print(2)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)
            continue

        if events[29] > 0 or events[30] > 0:
            print(17)
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)
            return

        print(48)
        return

if __name__ == "__main__":
    stabilize()