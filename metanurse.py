import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    def examine_vitals():
        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
            return
        if "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
            return
        if "BP" not in examined:
            take_action(27)
            examined.add("BP")
            return

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

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        if events[3] == 0 and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        if events[9] == 0 and "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            continue

        examine_vitals()

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)
                continue
            elif vitals["HR"] > 100:
                take_action(9)
                continue
            elif vitals["HR"] < 50:
                take_action(12)
                continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()