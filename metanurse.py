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
                    "Resps",
                ],
            )
        }

        # Airway assessment
        if "ExamineAirway" not in used_methods:
            print(3)
            used_methods.add("ExamineAirway")
            continue

        if not events[3]:  # No AirwayClear event
            print(35)
            continue

        # Breathing assessment
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

        if vitals["Sats"] and vitals["Sats"] < 88:
            if vitals["Sats"] < 65:  # Critical threshold, prepare CPR
                print(22)
            else:
                print(30)  # Non-rebreather mask for sats < 88%
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # Use Bag Valve Mask for low respiratory rate
            continue

        # Circulation assessment
        if "ExamineCirculation" not in used_methods:
            print(5)
            used_methods.add("ExamineCirculation")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            if vitals["MAP"] < 20:  # Critical threshold, prepare CPR
                print(22)
            else:
                print(15)  # Give fluids for low MAP
            continue

        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)  # Give Atropine for bradycardia
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(2)  # Check Rhythm for rates between 100 and 150
                continue
            elif vitals["HeartRate"] > 150:
                print(11)  # Give Amiodarone for high heart rate
                continue

        print(48)
        return

    print(48)

if __name__ == "__main__":
    main()