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
            observations[40:],
        )

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] != 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] != 0 else None,
            "CapillaryGlucose": vital_signs_values[2] if vital_signs_times[2] != 0 else None,
            "Temperature": vital_signs_values[3] if vital_signs_times[3] != 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] != 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] != 0 else None,
            "Resps": vital_signs_values[6] if vital_signs_times[6] != 0 else None,
        }

        if step == 0 or not initial_examine:
            print(3)
            initial_examine = True
            continue
        
        if not events[3]:
            print(35)
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)
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

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)
            continue

        if (vitals["HeartRate"] and vitals["HeartRate"] > 150) or any(events[i] for i in range(28, 39)):
            if "TurnOnDefibrillator" not in used_methods:
                print(39)
                used_methods.add("TurnOnDefibrillator")
                continue
            elif "DefibrillatorCharge" not in used_methods:
                print(40)
                used_methods.add("DefibrillatorCharge")
                continue
            else:
                print(43)
                continue

        print(48)
        return

    print(48)

if __name__ == "__main__":
    main()