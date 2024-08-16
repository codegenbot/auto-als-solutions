import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()
    actions_log = []

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            actions_log.append(0)
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

        # Emergency checks
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17) # Start CPR
            actions_log.append(17)
            continue

        # Examination steps
        if "airway" not in examined_vitals:
            take_action(3) # Examine airway
            examined_vitals.add("airway")
            actions_log.append(3)
            continue

        if "breathing" not in examined_vitals:
            take_action(4) # Examine breathing
            examined_vitals.add("breathing")
            actions_log.append(4)
            continue

        if "circulation" not in examined_vitals:
            take_action(5) # Examine circulation
            examined_vitals.add("circulation")
            actions_log.append(5)
            continue

        # Use tools to get measurements if needed
        if vitals["Sats"] is None and "SatsProbe" not in actions_log:
            take_action(25) # Use sats probe
            actions_log.append(25)
            continue

        if vitals["MAP"] is None and "BPCuff" not in actions_log:
            take_action(27) # Use blood pressure cuff
            actions_log.append(27)
            continue

        # Treatments based on measurements
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15) # Give fluids
            actions_log.append(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30 if "mask" not in actions_log else 29)
            actions_log.append(30 if "mask" not in actions_log else 29)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29) # Use bag valve mask
            actions_log.append(29)
            continue

        take_action(48) # Finish
        actions_log.append(48)
        break

if __name__ == "__main__":
    stabilize()