import sys

def main():
    max_steps = 350
    used_methods = set()
    initial_examine = False
    step_counter = 0

    def next_action(actions):
        for action in actions:
            if action not in used_methods:
                used_methods.add(action)
                return action
        return 0

    while step_counter < max_steps:
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if not initial_examine:
            actions = [3, 4, 5, 6, 7, 8]
            action = next_action(actions)
            if action:
                initial_examine = True
                step_counter += 1
                print(action)
                continue

        if "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
            step_counter += 1
            continue

        if "UseBloodPressureCuff" not in used_methods:
            print(27)
            used_methods.add("UseBloodPressureCuff")
            step_counter += 1
            continue

        if "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
            step_counter += 1
            continue

        if vitals["Sats"] and (vitals["Sats"] < 65 or (vitals["MAP"] is not None and vitals["MAP"] < 20)):
            print(17)
            step_counter += 1
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            step_counter += 1
            continue
        
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            step_counter += 1
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            if vitals["HeartRate"] and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
                if "TurnOnDefibrillator" not in used_methods:
                    print(39)
                    used_methods.add("TurnOnDefibrillator")
                    step_counter += 1
                    continue
                if "DefibrillatorCharge" not in used_methods:
                    print(40)
                    used_methods.add("DefibrillatorCharge")
                    step_counter += 1
                    continue
                if "DefibrillatorPace" not in used_methods:
                    print(43)
                    used_methods.add("DefibrillatorPace")
                    step_counter += 1
                    continue
            print(15)
            step_counter += 1
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return
        
        step_counter += 1
        print(48)
        return

if __name__ == "__main__":
    main()