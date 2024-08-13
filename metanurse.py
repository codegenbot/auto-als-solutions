import sys

def main():
    max_steps = 350
    used_methods = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )
        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "CapillaryGlucose": vital_signs_values[2] if vital_signs_times[2] > 0 else None,
            "Temperature": vital_signs_values[3] if vital_signs_times[3] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
            "Resps": vital_signs_values[6] if vital_signs_times[6] > 0 else None,
        }

        if "ExamineAirway" not in used_methods:
            print(3)
            used_methods.add("ExamineAirway")
            continue

        if not events[3]:
            print(35)
            continue

        if "OpenBreathingDrawer" not in used_methods:
            print(19)
            used_methods.add("OpenBreathingDrawer")
            continue

        if "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
            continue

        if "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            print(17)
            continue

        if vitals["Sats"] is None:
            print(25)
            continue

        if vitals["MAP"] is None:
            print(27)
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(2)
                continue
            elif vitals["HeartRate"] > 150:
                print(11)
                continue

        print(48)
        return
    
    print(48)

if __name__ == "__main__":
    main()