import sys

def main():
    max_steps = 350
    used_methods = set()
    initial_examine = {
        "airway": False,
        "breathing": False,
        "circulation": False,
        "disability": False,
        "exposure": False
    }

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if not initial_examine["airway"]:
            print(3)
            initial_examine["airway"] = True
            continue
        if not initial_examine["breathing"]:
            print(4)
            initial_examine["breathing"] = True
            continue
        if not initial_examine["circulation"]:
            print(5)
            initial_examine["circulation"] = True
            continue
        
        if not events[3]:  # If Airway is not clear
            print(35)
            continue

        if "UseSatsProbe" not in used_methods and not vitals["Sats"]:
            print(25)
            used_methods.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in used_methods and not vitals["MAP"]:
            print(27)
            used_methods.add("UseBloodPressureCuff")
            continue

        if "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
            continue

        if vitals["Sats"] and vitals["Sats"] < 65 or vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # Start Chest Compression
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            continue
        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)
            continue

        if (vitals["HeartRate"] and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50)) or events[27]:
            if "TurnOnDefibrillator" not in used_methods:
                print(39)
                used_methods.add("TurnOnDefibrillator")
                continue
            if "DefibrillatorCharge" not in used_methods:
                print(40)
                used_methods.add("DefibrillatorCharge")
                continue
            print(43)  # DefibrillatorPace
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return

        print(48)  # Ensure completion in the absence of other actions
        return

if __name__ == "__main__":
    main()