import sys

def stabilize():
    max_steps = 350
    actions_taken = {
        "examine_airway": False,
        "use_sats_probe": False,
        "use_blood_pressure_cuff": False,
        "view_monitor": False
    }

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if not actions_taken["examine_airway"]:
            actions_taken["examine_airway"] = True
            print(3)  # ExamineAirway
            continue
        
        if not actions_taken["use_sats_probe"]:
            actions_taken["use_sats_probe"] = True
            print(25)  # UseSatsProbe
            continue

        if not actions_taken["use_blood_pressure_cuff"]:
            actions_taken["use_blood_pressure_cuff"] = True
            print(27)  # UseBloodPressureCuff
            continue

        if not actions_taken["view_monitor"]:
            actions_taken["view_monitor"] = True
            print(16)  # ViewMonitor
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if vitals["HeartRate"] is not None:
                if vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50:
                    print(39)  # TurnOnDefibrillator
                    continue
                if 60 <= vitals["MAP"] <= 100:
                    print(43)  # DefibrillatorPace
                    continue
            print(15)  # GiveFluids
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return

    print(48)

if __name__ == "__main__":
    stabilize()