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
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "Glucose": values[2] if times[2] > 0 else None,
            "Temp": values[3] if times[3] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or \
           (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if "monitor" not in examined_vitals:
            take_action(16)
            examined_vitals.add("monitor")
            continue

        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(27)
            examined_vitals.add("MAP")
            continue

        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)
            examined_vitals.add("Sats")
            continue

        if vitals["RR"] is None and "RR" not in examined_vitals:
            take_action(4)
            examined_vitals.add("RR")
            continue

        if any(events[i] > 0 for i in range(3, 7)) and "airway" not in examined_vitals:
            take_action(3)
            examined_vitals.add("airway")
            continue

        if any(events[i] > 0 for i in range(7, 15)) and "breathing" not in examined_vitals:
            take_action(4)
            examined_vitals.add("breathing")
            continue

        if any(events[i] > 0 for i in range(15, 20)) and "circulation" not in examined_vitals:
            take_action(5)
            examined_vitals.add("circulation")
            continue

        if any(events[i] > 0 for i in range(20, 26)) and "disability" not in examined_vitals:
            take_action(6)
            examined_vitals.add("disability")
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30 if "mask" in examined_vitals else 29)
            examined_vitals.add("mask")
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()