import sys

def main():
    max_steps = 350
    used_methods, initial_examine, stepsTaken = set(), False, []

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

        if vitals["Sats"] and vitals["Sats"] < 65 or vitals["MAP"] and vitals["MAP"] < 20:
            stepsTaken.append(17)  # StartChestCompression
            break

        if step == 0 or not initial_examine:
            stepsTaken.append(3)  # ExamineAirway
            initial_examine = True
            continue

        if "UseSatsProbe" not in used_methods:
            stepsTaken.append(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in used_methods:
            stepsTaken.append(27)  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
            continue
        
        if "ViewMonitor" not in used_methods:
            stepsTaken.append(16)  # ViewMonitor
            used_methods.add("ViewMonitor")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            stepsTaken.append(15)  # GiveFluids
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 88:
            stepsTaken.append(30)  # UseNonRebreatherMask
            continue
            
        if any(events[i] for i in [29, 30, 32, 33, 35]):
            if "TurnOnDefibrillator" not in used_methods:
                stepsTaken.append(39)  # TurnOnDefibrillator
                used_methods.add("TurnOnDefibrillator")
                continue
            if "DefibrillatorCharge" not in used_methods:
                stepsTaken.append(40)  # DefibrillatorCharge
                used_methods.add("DefibrillatorCharge")
                continue
            if "DefibrillatorSync" not in used_methods:
                stepsTaken.append(47)  # DefibrillatorSync
                used_methods.add("DefibrillatorSync")
                continue
            if "DefibrillatorPace" not in used_methods:
                stepsTaken.append(43)  # DefibrillatorPace
                used_methods.add("DefibrillatorPace")
                continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])) and events[3]:
            stepsTaken.append(48)  # Finish
            break

        stepsTaken.append(48)  # Finish as ultimate fallback
        break

    for step in stepsTaken:
        print(step)

if __name__ == "__main__":
    main()