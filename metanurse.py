import sys

def stabilize():
    max_steps = 350
    actions = [3, 4, 5, 6, 7, 25, 27, 16]  # ExamineAirway, ExamineBreathing, ExamineCirculation, ExamineDisability, ExamineExposure, UseSatsProbe, UseBloodPressureCuff, ViewMonitor

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}
        
        if actions:
            print(actions.pop(0))
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
            print(15)  # GiveFluids
            continue
        
        if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
            print(43)  # DefibrillatorPace
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return
        
        # Re-evaluate if no specific action needed
        actions = [3, 4, 5, 6, 7, 25, 27, 16]
        print(0)  # DoNothing

if __name__ == "__main__":
    stabilize()