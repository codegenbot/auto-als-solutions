import sys

def stabilize():
    max_steps = 350
    examine_stage = 0
    used_probe = False
    used_cuff = False
    viewed_monitor = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if examine_stage == 0:
            examine_stage = 1
            print(3)  # ExamineAirway
            continue
        elif not used_probe:
            print(25)  # UseSatsProbe
            used_probe = True
            continue
        elif not used_cuff:
            print(27)  # UseBloodPressureCuff
            used_cuff = True
            continue
        elif not viewed_monitor:
            print(16)  # ViewMonitor
            viewed_monitor = True
            continue

        if vitals.get("Sats") < 65 or vitals.get("MAP") < 20:
            print(17)  # StartChestCompression
            continue
        if vitals.get("Sats") < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if vitals.get("RespRate") < 8:
            print(29)  # UseBagValveMask
            continue
        if vitals.get("MAP") < 60:
            print(15)  # GiveFluids
            continue
        if vitals.get("HeartRate") > 150 or events[32] > 0:  # Treat unstable tachyarrhythmia
            print(43)  # DefibrillatorPace
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)  # Finish
            return

        print(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()