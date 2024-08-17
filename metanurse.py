import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined = 350, set()

    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
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

        # Check for critical conditions first
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        # Examine Airway if not checked
        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)  # Examine Airway
            examined.add("Airway")
            continue

        # Ensure oxygen saturation measurement
        if "Sats" not in examined and vitals["Sats"] is None:
            take_action(25)  # Use Sats Probe
            examined.add("Sats")
            continue

        # Ensure MAP measurement
        if "MAP" not in examined and vitals["MAP"] is None:
            take_action(27)  # Use Blood Pressure Cuff
            examined.add("MAP")
            continue

        # Examine Breathing if not checked
        if "Breathing" not in examined:
            take_action(4)  # Examine Breathing
            examined.add("Breathing")
            continue

        # Treat oxygen saturation
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        # Treat hypotension
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        # Treat low respiratory rate
        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        # Treat heart rate abnormalities
        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)  # Use Monitor Pads (for cardioversion)
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # Give Atropine
                continue
            elif vitals["HR"] > 100:
                take_action(9)  # Give Adenosine
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()