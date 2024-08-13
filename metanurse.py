import sys


def stabilize():
    max_steps = 350
    assessed_sections = set()
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

        sequence = [
            (25, "UseSatsProbe"),
            (27, "UseBloodPressureCuff"),
            (16, "ViewMonitor"),
            (3, "ExamineAirway"),
            (4, "ExamineBreathing"),
            (5, "ExamineCirculation"),
            (6, "ExamineDisability"),
            (7, "ExamineExposure"),
        ]

        for action, action_name in sequence:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)
                break
        else:
            if vitals["Sats"] is not None and vitals["Sats"] < 65:
                print(22)
            elif vitals["MAP"] is not None and vitals["MAP"] < 20:
                print(15)
            elif vitals["MAP"] is not None and vitals["MAP"] < 60:
                if events[29] > 0 or events[30] > 0:
                    if 39 not in actions_taken:
                        actions_taken.add(39)
                        print(39)
                    elif 40 not in actions_taken:
                        actions_taken.add(40)
                        print(40)
                    else:
                        print(47)
                else:
                    print(15)
            elif vitals["Sats"] is not None and vitals["Sats"] < 88:
                print(30)
            elif vitals["RespRate"] is not None and vitals["RespRate"] < 8:
                print(29)
            elif all(
                vitals[name] is not None and vitals[name] >= threshold
                for name, threshold in zip(["Sats", "RespRate", "MAP"], [88, 8, 60])
            ):
                print(48)
                return
            else:
                print(48)
                return


if __name__ == "__main__":
    stabilize()