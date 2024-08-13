import sys

def main():
    def examine_initial(used_methods):
        if "ExamineAirway" not in used_methods:
            print(3); used_methods.add("ExamineAirway"); return
        if "ExamineBreathing" not in used_methods:
            print(4); used_methods.add("ExamineBreathing"); return
        if "ExamineCirculation" not in used_methods:
            print(5); used_methods.add("ExamineCirculation"); return
        if "UseSatsProbe" not in used_methods:
            print(25); used_methods.add("UseSatsProbe"); return
        if "UseBloodPressureCuff" not in used_methods:
            print(27); used_methods.add("UseBloodPressureCuff"); return
        if "ViewMonitor" not in used_methods:
            print(16); used_methods.add("ViewMonitor"); return
        return None

    max_steps = 350
    used_methods = set()
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
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"]
            )
        }

        initial_action = examine_initial(used_methods)
        if initial_action is not None:
            continue

        if not events[3]:  # AirwayClear
            print(35); continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17); continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15); continue

        if (vitals["HeartRate"] and vitals["HeartRate"] > 150) or events[27]:
            if "TurnOnDefibrillator" not in used_methods:
                print(39); used_methods.add("TurnOnDefibrillator"); continue
            elif "DefibrillatorCharge" not in used_methods:
                print(40); used_methods.add("DefibrillatorCharge"); continue
            elif "DefibrillatorSync" not in used_methods:
                print(47); used_methods.add("DefibrillatorSync"); continue
            else:
                print(43); continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30); continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29); continue

        print(48)
        return

    print(48)

if __name__ == "__main__":
    main()