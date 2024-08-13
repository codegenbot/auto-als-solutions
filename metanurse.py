import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}
        
        if "ExamineAirway" not in actions_taken:
            print(3)
            actions_taken.add("ExamineAirway")
            continue

        if "UseSatsProbe" not in actions_taken:
            print(25)
            actions_taken.add("UseSatsProbe")
            continue
        
        if "UseBloodPressureCuff" not in actions_taken:
            print(27)
            actions_taken.add("UseBloodPressureCuff")
            continue
        
        if "ViewMonitor" not in actions_taken:
            print(16)
            actions_taken.add("ViewMonitor")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return

    print(48)

if __name__ == "__main__":
    stabilize()