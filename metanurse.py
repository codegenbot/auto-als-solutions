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
        
        def examine_vital(vital, action_code):
            if vital not in examined:
                take_action(action_code)
                examined.add(vital)
                return True
            return False

        # Check for critical values
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        # Examine Airway
        if not any(events[3:7]) and examine_vital("Airway", 3):
            continue

        # Check Sats
        if examine_vital("Sats", 25) and vitals["Sats"] is None:
            continue

        # Check MAP
        if examine_vital("MAP", 27) and vitals["MAP"] is None:
            continue

        # Examine Breathing
        if examine_vital("Breathing", 4) and events[3]:
            continue

        # Use Monitor to get updated vital measurements
        if examine_vital("Monitor", 16):
            continue

        # Apply interventions based on vitals
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

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