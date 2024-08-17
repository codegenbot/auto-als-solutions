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
        values = observations[46:]

        vitals = {
            "HR": values[0] if observations[33] > 0 else None,
            "RR": values[1] if observations[34] > 0 else None,
            "Glucose": values[2] if observations[35] > 0 else None,
            "Temp": values[3] if observations[36] > 0 else None,
            "MAP": values[4] if observations[37] > 0 else None,
            "Sats": values[5] if observations[38] > 0 else None,
            "Resps": values[6] if observations[39] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        if not events[3]:  # If AirwayClear hasn't been detected:
            take_action(3)  # Examine Airway
            continue

        if "Sats" not in examined and vitals["Sats"] is None:
            take_action(25)  # Use Sats Probe
            examined.add("Sats")
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        if "MAP" not in examined and vitals["MAP"] is None:
            take_action(27)  # Use Blood Pressure Cuff
            examined.add("MAP")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if "HR" not in examined and vitals["HR"] is None:
            take_action(24)  # Use Monitor Pads
            examined.add("HR")
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if vitals["HR"] and vitals["HR"] > 150:
            take_action(24)  # Use Monitor Pads
            continue

        if vitals["Sats"] and vitals["Sats"] >= 88 and vitals["RR"] and vitals["RR"] >= 8 and vitals["MAP"] and vitals["MAP"] >= 60:
            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()