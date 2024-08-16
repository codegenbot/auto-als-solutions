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
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start CPR
            continue

        if "airway" not in examined_vitals:
            if any(events[i] > 0 for i in range(3, 7)):  # Assess airway issues
                take_action(3)  # Examine airway
                examined_vitals.add("airway")
                continue
            if not events[3]:  # Check if airway is clear
                take_action(35)  # Perform airway maneuvers
                continue

        if "breathing" not in examined_vitals:
            if any(events[i] > 0 for i in range(7, 15)):
                take_action(4)  # Examine breathing
                examined_vitals.add("breathing")
                continue
            if vitals["RR"] is None:
                take_action(4)  # Examine breathing rate
                examined_vitals.add("RR")
                continue
            if vitals["RR"] is not None and vitals["RR"] < 8:
                take_action(29)  # Use BagValveMask
                continue

        if "circulation" not in examined_vitals:
            if any(events[i] > 0 for i in range(15, 20)):
                take_action(5)  # Examine circulation
                examined_vitals.add("circulation")
                continue
            if vitals["MAP"] is None:
                take_action(27)  # Use blood pressure cuff
                examined_vitals.add("MAP")
                continue
            if vitals["MAP"] is not None and vitals["MAP"] < 60:
                take_action(15)  # Give fluids
                continue

        if "disability" not in examined_vitals:
            if any(events[i] > 0 for i in range(20, 26)):
                take_action(6)  # Examine disability
                examined_vitals.add("disability")
                continue

        if "exposure" not in examined_vitals:
            if any(events[i] > 0 for i in range(26, 33)):
                take_action(7)  # Examine exposure
                examined_vitals.add("exposure")
                continue

        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)  # Use sats probe
            examined_vitals.add("Sats")
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use NonRebreatherMask
            examined_vitals.add("mask")
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()