import sys

def stabilize():
    max_steps = 350
    actions = {
        "ExamineAirway": 3,
        "UseSatsProbe": 25,
        "UseBloodPressureCuff": 27,
        "ViewMonitor": 16,
        "StartChestCompression": 17,
        "GiveFluids": 15,
        "PerformCardioversion": 41,
        "UseNonRebreatherMask": 30,
        "UseBagValveMask": 29,
        "Finish": 48
    }

    steps = iter(actions.values())
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}
        
        if vitals["Sats"] is not None and vitals["Sats"] < 65 or vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(actions["StartChestCompression"])
            continue

        if vitals["HeartRate"] is not None and vitals["HeartRate"] > 150:
            print(actions["PerformCardioversion"])
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(actions["GiveFluids"])
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(actions["UseNonRebreatherMask"])
            continue
        
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(actions["UseBagValveMask"])
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(actions["Finish"])
            return

        print(next(steps, actions["Finish"]))

if __name__ == "__main__":
    stabilize()