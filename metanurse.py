import sys


def stabilize():
    max_steps = 350
    steps = 0
    examine_airway = examine_breathing = examine_circulation = False
    use_sats_probe = use_blood_pressure_cuff = view_monitor = False

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

        if not examine_airway:
            print(3)
            examine_airway = True
        elif not examine_breathing:
            print(4)
            examine_breathing = True
        elif not examine_circulation:
            print(5)
            examine_circulation = True
        elif vitals["Sats"] is None and not use_sats_probe:
            print(25)
            use_sats_probe = True
        elif vitals["MAP"] is None and not use_blood_pressure_cuff:
            print(27)
            use_blood_pressure_cuff = True
        elif not view_monitor:
            print(16)
            view_monitor = True
        elif vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)
        elif vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)
        elif vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)
        elif vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)
        elif vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)
        elif vitals["HeartRate"] is not None and (
            vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50
        ):
            print(43)
        elif all(
            [
                vitals["Sats"] is not None and vitals["Sats"] >= 88,
                vitals["RespRate"] is not None and vitals["RespRate"] >= 8,
                vitals["MAP"] is not None and vitals["MAP"] >= 60,
            ]
        ):
            print(48)
            return
        else:
            print(1)

        steps += 1


if __name__ == "__main__":
    stabilize()