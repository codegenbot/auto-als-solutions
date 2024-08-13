import sys

def stabilize():
    max_steps = 350
    step = 0
    examinations_done = {
        "airway": False,
        "sats_probe": False,
        "blood_pressure_cuff": False,
        "monitor": False,
    }

    while step < max_steps:
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

        if not examinations_done["airway"]:
            print(3)
            examinations_done["airway"] = True
            step += 1
            continue

        if not examinations_done["sats_probe"]:
            print(25)
            examinations_done["sats_probe"] = True
            step += 1
            continue

        if not examinations_done["blood_pressure_cuff"]:
            print(27)
            examinations_done["blood_pressure_cuff"] = True
            step += 1
            continue

        if not examinations_done["monitor"]:
            print(16)
            examinations_done["monitor"] = True
            step += 1
            continue

        sats = vitals.get("Sats")
        map_ = vitals.get("MAP")
        heart_rate = vitals.get("HeartRate")
        resp_rate = vitals.get("RespRate")

        if (sats is not None and sats < 65) or (map_ is not None and map_ < 20):
            print(17)
            step += 1
            continue

        if map_ is not None and map_ < 60:
            print(15)
            step += 1
            continue

        if sats is not None and sats < 88:
            print(30)
            step += 1
            continue

        if resp_rate is not None and resp_rate < 8:
            print(29)
            step += 1
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [sats, resp_rate, map_], [88, 8, 60]
            )
        ):
            print(48)
            return

        step += 1

if __name__ == "__main__":
    stabilize()