import sys


def stabilize():
    max_steps = 350
    examine_airway = (
        examine_breathing
    ) = examine_circulation = examine_disability = False
    use_sats_probe = use_blood_pressure_cuff = view_monitor = False

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

        if not examine_airway:
            examine_airway = True
            print(3)
            continue

        if not examine_breathing:
            examine_breathing = True
            print(4)
            continue

        if not examine_circulation:
            examine_circulation = True
            print(5)
            continue

        if vitals["Sats"] is None and not use_sats_probe:
            print(25)
            use_sats_probe = True
            continue

        if vitals["MAP"] is None and not use_blood_pressure_cuff:
            print(27)
            use_blood_pressure_cuff = True
            continue

        if not view_monitor:
            view_monitor = True
            print(16)
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

        if vitals["HeartRate"] is not None and vitals["HeartRate"] > 150:
            print(43)
            continue

        if vitals["HeartRate"] is not None and vitals["HeartRate"] < 50:
            print(43)
            continue

        if all(
            [
                vitals["Sats"] is not None and vitals["Sats"] >= 88,
                vitals["RespRate"] is not None and vitals["RespRate"] >= 8,
                vitals["MAP"] is not None and vitals["MAP"] >= 60,
            ]
        ):
            print(48)
            return

        print(48)
        return


if __name__ == "__main__":
    stabilize()