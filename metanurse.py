import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

    actions_priority = [
        (15, "vitals['MAP'] is not None and vitals['MAP'] < 60", 27),  # Give fluids if MAP < 60
        (3, "airway not in examined_vitals", 5),  # Examine Airway
        (4, "breathing not in examined_vitals", 6),  # Examine Breathing
        (25, "Sats not in examined_vitals"),  # Use Sats Probe
        (29, "vitals['RR'] is not None and vitals['RR'] < 8"),  # Bag-Valve Mask if RR < 8
        (30, "vitals['Sats'] is not None and vitals['Sats'] < 88", 27),  # NonRebreatherMask if Sats < 88
        (5, "circulation not in examined_vitals", 6),  # Examine Circulation
        (38, "MAP not in examined_vitals")  # Take BP
    ]

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # Start CPR
            continue

        for action, condition, fallback in actions_priority:
            if eval(condition):
                take_action(action)
                examined_vitals.add(condition)
                break
        else:
            take_action(48)
            break

if __name__ == "__main__":
    stabilize()