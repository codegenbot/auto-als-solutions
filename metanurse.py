import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined = 350, set()
    for step in range(steps):
        try:
            observations = list(map(float, input().strip().split()))
        except:
            take_action(48)
            return
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        measurements = observations[46:]

        vitals = {
            "HR": measurements[0] if observations[33] > 0 else None,
            "RR": measurements[1] if observations[34] > 0 else None,
            "Glucose": measurements[2] if observations[35] > 0 else None,
            "Temp": measurements[3] if observations[36] > 0 else None,
            "MAP": measurements[4] if observations[37] > 0 else None,
            "Sats": measurements[5] if observations[38] > 0 else None,
            "Resps": measurements[6] if observations[39] > 0 else None,
        }

        # Check for critical conditions and take immediate action
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        # Examine Airway
        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        # Probe for missing measurements (Sats and MAP)
        if "Sats" not in examined and vitals["Sats"] is None:
            take_action(25)
            examined.add("Sats")
            continue

        if "MAP" not in examined and vitals["MAP"] is None:
            take_action(27)
            examined.add("MAP")
            continue

        # View monitor for all current stats
        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
            continue

        # Examine Breathing
        if "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            continue

        # Corrective measures based on vitals
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask for low oxygen saturation
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give fluids for low MAP
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use bag valve mask for low respiratory rate
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)  # Use monitor pads for tachyarrhythmia
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # Use atropine for bradycardia
                continue
            elif vitals["HR"] > 100:
                take_action(9)   # Use adenosine for a stable tachycardia
                continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()