import sys

def main():
    max_steps = 350
    initial_examine = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}
        
        if step == 0 or not initial_examine:
            for action in [3, 4, 5]:  # Examine Airway, Breathing, Circulation
                print(action)
                initial_examine = True
                break
            continue
        
        if "UseSatsProbe" not in locals():
            print(25)
            locals()["UseSatsProbe"] = True
            continue

        if "UseBloodPressureCuff" not in locals():
            print(27)
            locals()["UseBloodPressureCuff"] = True
            continue

        if "ViewMonitor" not in locals():
            print(16)
            locals()["ViewMonitor"] = True
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
            if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
                if "TurnOnDefibrillator" not in locals():
                    print(39)
                    locals()["TurnOnDefibrillator"] = True
                    continue
                if "DefibrillatorCharge" not in locals():
                    print(40)
                    locals()["DefibrillatorCharge"] = True
                    continue
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
        return

if __name__ == "__main__":
    main()