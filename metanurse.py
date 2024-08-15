import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    critical_events = set(range(26, 33))  # Events indicating rhythm

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
            take_action(17)  # Start Chest Compression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 25 not in actions_taken:
                actions_taken.add(25)
                take_action(25)  # Use Sats Probe
            else:
                take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if 27 not in actions_taken:
                actions_taken.add(27)
                take_action(27)  # Use Blood Pressure Cuff
            else:
                take_action(15)  # Give Fluids
            continue

        if any(events[i] > 0 for i in critical_events):
            take_action(2)  # Check Rhythm
            continue

        examinations = [(27, 38), (25, 16), (16, 5), (38, 3)]
        for action1, action2 in examinations:
            if action1 not in actions_taken:
                actions_taken.add(action1)
                take_action(action1)
                break
            elif action2 not in actions_taken:
                actions_taken.add(action2)
                take_action(action2)
                break
        else:
            if any(events[i] > 0 for i in range(3, 7)):
                take_action(3)  # Examine Airway
                continue
            if any(events[i] > 0 for i in range(7, 15)):
                take_action(4)  # Examine Breathing
                continue

            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()