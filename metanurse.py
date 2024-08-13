import sys

def main():
    max_steps = 350
    used_methods = set()
    initial_examine = False
    examine_list = [3, 4, 5, 6, 7]

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if step == 0 or not initial_examine:
            print(examine_list[step % len(examine_list)])
            initial_examine = True
            continue
        
        # Ensure proper initial examinations
        if "ExamineAirway" not in used_methods:
            print(3)
            used_methods.add("ExamineAirway")
            continue
        if "ExamineBreathing" not in used_methods:
            print(4)
            used_methods.add("ExamineBreathing")
            continue
        if "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
            continue
        if "UseBloodPressureCuff" not in used_methods:
            print(27)
            used_methods.add("UseBloodPressureCuff")
            continue
        if "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
            continue

        # ABCDE protocol
        if vitals["Sats"] is not None and vitals["Sats"] < 65 or vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # Cardiac arrest, start CPR
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # Administer oxygen with non-rebreather mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # Use bag-valve mask for ventilation
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
                if "TurnOnDefibrillator" not in used_methods:
                    print(39)
                    used_methods.add("TurnOnDefibrillator")
                    continue
                if "DefibrillatorCharge" not in used_methods:
                    print(40)
                    used_methods.add("DefibrillatorCharge")
                    continue
                print(43)  # Use defibrillator to pace heart
                continue
            print(15)  # Administer intravenous fluids
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return
        
        print(48)
        return

if __name__ == "__main__":
    main()