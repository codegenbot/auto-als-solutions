import sys


def stabilize():
    max_steps = 350
    examined_airway = False
    used_sats_probe = used_blood_pressure_cuff = viewed_monitor = False

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
            print(3)  # ExamineAirway
            continue

        if not used_sats_probe:
            print(25)  # UseSatsProbe
            used_sats_probe = True
            continue

        if not used_blood_pressure_cuff:
            print(27)  # UseBloodPressureCuff
            used_blood_pressure_cuff = True
            continue

        if not viewed_monitor:
            print(16)  # ViewMonitor
            viewed_monitor = True
            continue

        # Check for critical situations
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        # Stabilization treatment
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["HeartRate"] is not None and (
            vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50
        ):
            print(39)  # TurnOnDefibrillator
            continue

        if vitals["HeartRate"] is not None and 60 <= vitals["HeartRate"] <= 100:
            print(43)  # DefibrillatorPace
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

    print(48)  # Finish to avoid technical failure


if __name__ == "__main__":
    stabilize()