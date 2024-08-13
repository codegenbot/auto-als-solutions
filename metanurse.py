import sys

def stabilize():
    max_steps = 350
    first_examine = False
    use_sats_probe = use_blood_pressure_cuff = view_monitor = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
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
                    "Resps"
                ],
            )
        }

        if step == 0 or not first_examine:
            print(3)  # ExamineAirway
            first_examine = True
            continue

        if not use_sats_probe:
            print(25)  # UseSatsProbe
            use_sats_probe = True
            continue

        if not use_blood_pressure_cuff:
            print(27)  # UseBloodPressureCuff
            use_blood_pressure_cuff = True
            continue

        if not view_monitor:
            print(16)  # ViewMonitor
            view_monitor = True
            continue

        sats = vitals["Sats"]
        map_ = vitals["MAP"]
        heart_rate = vitals["HeartRate"]
        resp_rate = vitals["RespRate"]

        if sats is not None and sats < 65:
            print(17)  # StartChestCompression
            continue

        if map_ is not None and map_ < 20:
            print(17)  # StartChestCompression
            continue

        # New additions: treat specific conditions if found
        if heart_rate is not None and (heart_rate > 150 or heart_rate < 50):
            print(40)  # DefibrillatorCharge
            continue
        
        if map_ is not None and map_ < 60:
            print(15)  # GiveFluids
            continue

        if sats is not None and sats < 92:
            print(30)  # UseNonRebreatherMask
            continue

        if resp_rate is not None and resp_rate < 8:
            print(29)  # UseBagValveMask
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [sats, resp_rate, map_], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

    print(48)  # Finish

if __name__ == "__main__":
    stabilize()