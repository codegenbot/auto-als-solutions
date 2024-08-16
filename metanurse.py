import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] != 0 else None,
            "RR": values[1] if times[1] != 0 else None,
            "Glucose": values[2] if times[2] != 0 else None,
            "Temp": values[3] if times[3] != 0 else None,
            "MAP": values[4] if times[4] != 0 else None,
            "Sats": values[5] if times[5] != 0 else None,
            "Resps": values[6] if times[6] != 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue
        
        if "airway" not in examined_vitals:
            if any(events[i] > 0 for i in [3, 7, 8, 9]):
                take_action(3)
                examined_vitals.add("airway")
                continue
            if any(events[i] > 0 for i in [5, 6, 10]):
                take_action(18)
                continue
            take_action(35)
            continue

        if "breathing" not in examined_vitals:
            if vitals["Sats"] is None:
                take_action(25)
                continue
            if vitals["Sats"] < 88:
                take_action(30)
                continue
            if vitals["RR"] < 8:
                take_action(29)
                continue
            take_action(4)
            examined_vitals.add("breathing")
            continue

        if "circulation" not in examined_vitals:
            if vitals["MAP"] is None:
                take_action(27)
                continue
            if vitals["MAP"] < 60:
                take_action(15)
                continue
            take_action(5)
            examined_vitals.add("circulation")
            continue

        if "disability" not in examined_vitals:
            take_action(6)
            examined_vitals.add("disability")
            continue

        if "exposure" not in examined_vitals:
            take_action(7)
            examined_vitals.add("exposure")
            continue
            
        take_action(48)
        break

if __name__ == "__main__":
    stabilize()