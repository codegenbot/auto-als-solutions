import sys


def stabilize():
    max_steps = 350

    use_sats_probe = use_blood_pressure_cuff = view_monitor = False
    examined_airway = examined_breathing = False

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

        if not examined_airway:
            examined_airway = True
            print(3)
            continue

        if not examined_breathing:
            examined_breathing = True
            print(4)
            continue

        if not use_sats_probe:
            print(25)
            use_sats_probe = True
            continue

        if not use_blood_pressure_cuff:
            print(27)
            use_blood_pressure_cuff = True
            continue

        if not view_monitor:
            print(16)
            view_monitor = True
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if vitals["HeartRate"] is not None and vitals["HeartRate"] > 150:
                print(40)
                continue
            print(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)
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