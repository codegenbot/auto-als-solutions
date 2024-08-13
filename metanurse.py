import sys

def main():
    max_steps = 350
    used_methods = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"])}

        if "ExamineAirway" not in used_methods:
            print(3)
            used_methods.add("ExamineAirway")
            continue

        if not events[3]:  # Airway not clear
            if events[5] or events[6]:  # Vomit/Blood in airway
                print(31)
                continue
            elif events[8]:  # Tongue obstructing
                print(36)
                continue
            else:
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

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)  # Start chest compression
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # Use non-rebreather mask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # Use bag valve mask
            continue

        if "ExamineCirculation" not in used_methods:
            print(5)
            used_methods.add("ExamineCirculation")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # Give fluids
            continue

        if "ExamineResponse" not in used_methods:
            print(8)
            used_methods.add("ExamineResponse")
            continue

        if "CheckRhythm" not in used_methods:
            print(2)
            used_methods.add("CheckRhythm")
            continue

        if vitals["HeartRate"] is not None:
            if vitals["HeartRate"] < 50:
                print(12)  # Give atropine
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(9)  # Give adenosine (assume SVT)
                continue
            elif vitals["HeartRate"] > 150:
                print(9)  # Give adenosine (assume SVT)
                continue

        if vitals["HeartRate"] is None and events[18]:  # No radial pulse
            print(17)  # Start chest compression
            continue

        if vitals["MAP"] and vitals["MAP"] >= 60 and vitals["Sats"] >= 88 and vitals["RespRate"] >= 8:
            print(48)  # Finish if patient is stable
            return

    print(48)  # Finish after max_steps

if __name__ == "__main__":
    main()