import sys


def stabilize():
    max_steps = 350
    steps = 0
    actions_taken = set()

    while steps < max_steps:
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

        actions = [
            (25, "UseSatsProbe"),
            (27, "UseBloodPressureCuff"),
            (16, "ViewMonitor"),
            (3, "ExamineAirway"),
            (4, "ExamineBreathing"),
            (5, "ExamineCirculation"),
            (6, "ExamineDisability"),
            (7, "ExamineExposure"),
            (8, "ExamineResponse"),
        ]

        for action, _ in actions:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)
                steps += 1
                break
        else:
            if vitals["Sats"] and vitals["Sats"] < 65:
                print(22)
                steps += 1
                continue
            if vitals["MAP"] and vitals["MAP"] < 20:
                print(15)
                steps += 1
                continue

            if vitals["MAP"] and vitals["MAP"] < 60:
                if events[29] > 0 or events[30] > 0:
                    print(10)
                else:
                    print(15)
                steps += 1
                continue

            if vitals["Sats"] and vitals["Sats"] < 88:
                print(30)
                steps += 1
                continue

            if vitals["RespRate"] and vitals["RespRate"] < 8:
                print(29)
                steps += 1
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