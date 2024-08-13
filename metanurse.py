import sys

def stabilize():
    max_steps = 350
    assessments = {"A": False, "B": False, "C": False, "D": False, "E": False}
    measures_taken = {"use_sats_probe": False, "use_blood_pressure_cuff": False, "view_monitor": False}
    treatments = {"give_fluids": False, "use_non_rebreather_mask": False, "use_bag_valve_mask": False, "defibrillator_pace": False}

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {name: (value if time > 0 else None) for value, time, name in zip(
            vital_signs_values, vital_signs_times, [
                "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
            ]
        )}

        if not assessments["A"]:
            assessments["A"] = True
            print(3)  # ExamineAirway
            continue

        if not measures_taken["use_sats_probe"]:
            print(25)  # UseSatsProbe
            measures_taken["use_sats_probe"] = True
            continue

        if not measures_taken["use_blood_pressure_cuff"]:
            print(27)  # UseBloodPressureCuff
            measures_taken["use_blood_pressure_cuff"] = True
            continue

        if not measures_taken["view_monitor"]:
            print(16)  # ViewMonitor
            measures_taken["view_monitor"] = True
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60 and not treatments["give_fluids"]:
            treatments["give_fluids"] = True
            print(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88 and not treatments["use_non_rebreather_mask"]:
            treatments["use_non_rebreather_mask"] = True
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8 and not treatments["use_bag_valve_mask"]:
            treatments["use_bag_valve_mask"] = True
            print(29)  # UseBagValveMask
            continue

        if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50) and not treatments["defibrillator_pace"]:
            treatments["defibrillator_pace"] = True
            print(43)  # DefibrillatorPace
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)  # Finish
            return

if __name__ == "__main__":
    stabilize()