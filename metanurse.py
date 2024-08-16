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
            take_action(17)  # Start chest compressions
            continue

        # Start with fundamental examinations
        if "response" not in examined_vitals:
            take_action(8)  # Examine Response
            examined_vitals.add("response")
            continue

        if "airway" not in examined_vitals:
            take_action(3)  # Examine Airway
            examined_vitals.add("airway")
            continue

        if "breathing" not in examined_vitals:
            take_action(4)  # Examine Breathing
            examined_vitals.add("breathing")
            continue

        if "circulation" not in examined_vitals:
            take_action(5)  # Examine Circulation
            examined_vitals.add("circulation")
            continue

        if "disability" not in examined_vitals:
            take_action(6)  # Examine Disability
            examined_vitals.add("disability")
            continue

        if "exposure" not in examined_vitals:
            take_action(7)  # Examine Exposure
            examined_vitals.add("exposure")
            continue

        # Ensure monitoring
        if "monitor" not in examined_vitals:
            take_action(16)  # View Monitor
            examined_vitals.add("monitor")
            continue

        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(27)  # Use Blood Pressure Cuff
            examined_vitals.add("MAP")
            continue

        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)  # Use Sats Probe
            examined_vitals.add("Sats")
            continue

        if vitals["RR"] is None and "RR" not in examined_vitals:
            take_action(4)  # Re-examine Breathing
            examined_vitals.add("RR")
            continue

        # Check for treatments based on vital measurements
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30 if "mask" in examined_vitals else 29)  # Use Non-Rebreather Mask or Bag-Valve Mask
            examined_vitals.add("mask")
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()