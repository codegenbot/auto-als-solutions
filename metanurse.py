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

    steps, examined = 350, set()

    for _ in range(steps):
        observations = get_observations()
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        measured_recent = observations[33:40]
        measurements = observations[40:]

        vitals = {
            "HR": measurements[0] if measured_recent[0] > 0 else None,
            "RR": measurements[1] if measured_recent[1] > 0 else None,
            "Glucose": measurements[2] if measured_recent[2] > 0 else None,
            "Temp": measurements[3] if measured_recent[3] > 0 else None,
            "MAP": measurements[4] if measured_recent[4] > 0 else None,
            "Sats": measurements[5] if measured_recent[5] > 0 else None,
            "Resps": measurements[6] if measured_recent[6] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start chest compressions
            continue

        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)  # Examine airway
            examined.add("Airway")
            continue

        if vitals["Sats"] is None and "Sats" not in examined:
            take_action(25)  # UseSatsProbe
            examined.add("Sats")
            continue
        
        if vitals["MAP"] is None and "MAP" not in examined:
            take_action(27)  # UseBloodPressureCuff
            examined.add("MAP")
            continue

        if "Breathing" not in examined:
            take_action(4)  # Examine breathing
            examined.add("Breathing")
            continue

        if vitals["Sats"] is None or vitals["MAP"] is None:
            take_action(16)  # ViewMonitor to see sats and MAP
            continue

        if vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue
        
        if vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if vitals["RR"] < 8:
            take_action(29)  # Use bag valve mask
            continue

        if any(events[27:33]):
            take_action(24)  # Use defibrillator (e.g., for arrhythmias)
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)  # Use defibrillator for cardioversion
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # Give atropine
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()