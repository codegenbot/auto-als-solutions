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

        # Airway
        if "ExamineAirway" not in used_methods:
            print(3)
            used_methods.add("ExamineAirway")
            continue

        if not events[3]:
            print(35)
            continue

        # Breathing
        if "ExamineBreathing" not in used_methods:
            print(4)
            used_methods.add("ExamineBreathing")
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

        # Vital checks
        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            print(17)  # Start CPR
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # Use Bag Valve Mask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # Give Fluids
            continue

        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)  # Give Atropine
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(2)  # Check Rhythm
                continue
            elif vitals["HeartRate"] > 150:
                print(9)  # Give Adenosine
                continue

        print(48)  # Finish
        return

    print(48)

if __name__ == "__main__":
    main()