import sys

def stabilize():
    max_steps = 350

    use_sats_probe = use_blood_pressure_cuff = view_monitor = False
    examined_airway = examined_breathing = examined_circulation = False

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
            print(3)
            examined_airway = True
            continue

        if not examined_breathing:
            print(4)
            examined_breathing = True
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
            print(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)
            continue
        
        if all(vitals[key] is not None for key in ["Sats", "RespRate", "MAP"]) and all(
            vitals[key] >= threshold for key, threshold in [("Sats", 88), ("RespRate", 8), ("MAP", 60)]
        ):
            print(48)
            return

        print(48)
        return

if __name__ == "__main__":
    stabilize()