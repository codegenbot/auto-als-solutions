import sys

def main():
    max_steps = 350
    used_methods = set()
    initial_examine = False

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

        if step == 0 or not initial_examine:
            print(3)  # ExamineAirway
            initial_examine = True
            continue

        if "UseSatsProbe" not in used_methods:
            print(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in used_methods:
            print(27)  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
            continue
        
        if "ViewMonitor" not in used_methods:
            print(16)  # ViewMonitor
            used_methods.add("ViewMonitor")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            used_methods.add("UseNonRebreatherMask")
            continue
        
        defibrillation_process = ["TurnOnDefibrillator", "DefibrillatorCharge", "DefibrillatorSync", "DefibrillatorPace"]
        if any(events[i+28] > 0 for i in [6, 7, 8, 11]) and not all(m in used_methods for m in defibrillation_process):
            if "TurnOnDefibrillator" not in used_methods:
                print(39)  # TurnOnDefibrillator
                used_methods.add("TurnOnDefibrillator")
                continue
            if "DefibrillatorCharge" not in used_methods:
                print(40)  # DefibrillatorCharge
                used_methods.add("DefibrillatorCharge")
                continue
            if "DefibrillatorSync" not in used_methods:
                print(47)  # DefibrillatorSync
                used_methods.add("DefibrillatorSync")
                continue
            if "DefibrillatorPace" not in used_methods:
                print(43)  # DefibrillatorPace
                used_methods.add("DefibrillatorPace")
                continue
        
        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])) and events[3]:
            print(48)  # Finish
            return

        print(48)  # Finish as ultimate fallback
        return

if __name__ == "__main__":
    main()