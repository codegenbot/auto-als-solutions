import sys

def main():
    max_steps = 350
    used_methods = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if step == 0:
            print(3)
        elif step == 1:
            print(4)
        elif step == 2:
            print(5)
        elif "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
        elif "UseBloodPressureCuff" not in used_methods:
            print(27)
            used_methods.add("UseBloodPressureCuff")
        elif "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
        else:
            if vitals["Sats"] is not None and (vitals["Sats"] < 65 or (vitals["MAP"] is not None and vitals["MAP"] < 20)):
                print(17)
            elif vitals["Sats"] is not None and vitals["Sats"] < 88:
                print(30)
            elif vitals["RespRate"] is not None and vitals["RespRate"] < 8:
                print(29)
            elif vitals["MAP"] is not None and vitals["MAP"] < 60:
                if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
                    if "TurnOnDefibrillator" not in used_methods:
                        print(39)
                        used_methods.add("TurnOnDefibrillator")
                    elif "DefibrillatorCharge" not in used_methods:
                        print(40)
                        used_methods.add("DefibrillatorCharge")
                    else:
                        print(43)
                else:
                    print(15)
            elif all(vital is not None and vital >= threshold for vital, threshold in zip(
                    [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                    [88, 8, 60])):
                print(48)
                return
            else:
                print(48)
                return

if __name__ == "__main__":
    main()