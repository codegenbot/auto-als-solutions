import sys

def stabilize():
    max_steps = 350

    first_examine = use_sats_probe = use_blood_pressure_cuff = view_monitor = False
    airway_examined = breathing_examined = circulation_examined = disability_examined = False

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

        if not first_examine:
            first_examine = True
            print(3)  # ExamineAirway
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

        if not airway_examined:
            print(3)  # ExamineAirway
            airway_examined = True
            continue

        if not breathing_examined:
            print(4)  # ExamineBreathing
            breathing_examined = True
            continue

        if not circulation_examined:
            print(5)  # ExamineCirculation
            circulation_examined = True
            continue 
        
        if not disability_examined:
            print(6)  # ExamineDisability
            disability_examined = True
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["HeartRate"] is not None and vitals["HeartRate"] > 150:
            print(10)  # GiveAdrenaline
            continue
        
        if vitals["HeartRate"] is not None and vitals["HeartRate"] < 50:
            print(12)  # GiveAtropine
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

        print(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()