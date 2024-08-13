import sys

def main():
    max_steps = 350
    used_methods = set()
    initial_examine = False
    assessed_airway = False
    examined = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
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
                    "Resps"
                ]
            )
        }
        
        unstable_rhythms = [28, 31, 32, 35, 36, 37]

        if step == 0 or not examined:
            print(3)
            examined = True
            continue
        
        if events[7]:
            print(29)
            continue
        
        if not assessed_airway:
            if not events[3]:
                print(35)
                continue
            assessed_airway = True
        
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

        needs_chest_compression = (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20)
        if needs_chest_compression:
            print(17)
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

        if any(events[i] for i in unstable_rhythms):
            if "TurnOnDefibrillator" not in used_methods:
                print(39)
                used_methods.add("TurnOnDefibrillator")
                continue
            if "DefibrillatorCharge" not in used_methods:
                print(40)
                used_methods.add("DefibrillatorCharge")
                continue
            print(47)
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return
        
        print(1)
        continue

if __name__ == "__main__":
    main()