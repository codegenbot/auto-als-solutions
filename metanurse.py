import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def get_observations():
        try:
            return list(map(float, input().strip().split()))
        except Exception:
            take_action(48)
            sys.exit()

    steps = 350
    examined = {"Airway": False, "Breathing": False, "Circulation": False, "HeartRate": False, "Sats": False, "MAP": False}

    for _ in range(steps):
        observations = get_observations()
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        measured_recent = observations[33:40]
        measurements = observations[46:]

        vitals = {
            "HR": measurements[0] if measured_recent[0] > 0 else None,
            "RR": measurements[1] if measured_recent[1] > 0 else None,
            "Glucose": measurements[2] if measured_recent[2] > 0 else None,
            "Temp": measurements[3] if measured_recent[3] > 0 else None,
            "MAP": measurements[4] if measured_recent[4] > 0 else None,
            "Sats": measurements[5] if measured_recent[5] > 0 else None,
            "Resps": measurements[6] if measured_recent[6] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if not examined["Airway"]:
            take_action(3)
            examined["Airway"] = True
            continue

        if not vitals["Sats"] and not examined["Sats"]:
            take_action(25)
            examined["Sats"] = True
            continue
        
        if not vitals["MAP"] and not examined["MAP"]:
            take_action(27)
            examined["MAP"] = True
            continue

        if not vitals["RR"] and not examined["Breathing"]:
            take_action(4)
            examined["Breathing"] = True
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["HR"] and not examined["HeartRate"]:
            take_action(16)
            examined["HeartRate"] = True
            continue

        if vitals["HR"] and vitals["HR"] > 150:
            take_action(24)
            continue

        if vitals["HR"] and vitals["HR"] < 50:
            take_action(12)
            continue

        if events[31] > 0:  # Assuming HeartRhythmNSR
            take_action(16)
            continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()