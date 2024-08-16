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
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start CPR
            continue

        if "airway" not in examined:
            take_action(3)  # Examine airway
            examined.add("airway")
            continue

        if "Sats" not in examined:
            take_action(25)  # Use Sats Probe
            examined.add("Sats")
            continue

        if "MAP" not in examined:
            take_action(27)  # Use Blood Pressure Cuff
            examined.add("MAP")
            continue

        if "breathing" not in examined and "Sats" in examined:
            take_action(4)  # Examine breathing
            examined.add("breathing")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use NonRebreatherMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["RR"] is None:
            take_action(4)  # Examine breathing
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use BagValveMask
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()