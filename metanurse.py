import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "Glucose": values[2] if times[2] > 0 else None,
            "Temp": values[3] if times[3] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
            continue

        if not vitals["MAP"]:
            if "BP" not in examined:
                take_action(27)
                examined.add("BP")
                continue

        if not vitals["Sats"]:
            if "SatsProbe" not in examined:
                take_action(25)
                examined.add("SatsProbe")
                continue
        
        if events[3] == 0 and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        if "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            continue

        if "Circulation" not in examined:
            take_action(5)
            examined.add("Circulation")
            continue

        if not all([vitals["MAP"], vitals["Sats"], vitals["RR"], vitals["HR"]]):
            continue

        if vitals["HR"] and (vitals["HR"] > 150 or vitals["HR"] < 50):
            take_action(24)
            continue

        if vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] < 8:
            take_action(29)
            continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()