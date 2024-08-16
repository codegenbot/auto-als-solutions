import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    def measure_vitals():
        if "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
        elif "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
        elif "Circulation" not in examined:
            take_action(5)
            examined.add("Circulation")
        elif "Disability" not in examined:
            take_action(6)
            examined.add("Disability")
        elif "Exposure" not in examined:
            take_action(7)
            examined.add("Exposure")
        elif "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
        elif "BP" not in examined:
            take_action(27)
            examined.add("BP")
        elif "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
        elif "RespRate" not in examined:
            take_action(4)
            examined.add("RespRate")

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = dict()
        vitals["HR"] = values[0] if times[0] > 0 else None
        vitals["RR"] = values[1] if times[1] > 0 else None
        vitals["Glucose"] = values[2] if times[2] > 0 else None
        vitals["Temp"] = values[3] if times[3] > 0 else None
        vitals["MAP"] = values[4] if times[4] > 0 else None
        vitals["Sats"] = values[5] if times[5] > 0 else None
        vitals["Resps"] = values[6] if times[6] > 0 else None

        if vitals["Sats"] and vitals["Sats"] < 65 or vitals["MAP"] and vitals["MAP"] < 20:
            take_action(17)
            continue

        measure_vitals()

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        heart_rhythm_event_indices = range(29, 39)
        if any(events[i] > 0 for i in heart_rhythm_event_indices):
            take_action(28)
            continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()