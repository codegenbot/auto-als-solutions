import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    measurements_needed = {27: "MAP", 25: "Sats", 16: "Monitor"}
    
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
        
        # Immediate CPR if critical
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        # Check necessary vitals first
        for action, vital in measurements_needed.items():
            if vital not in actions_taken and (vitals[vital] is None or values[measurements_needed[action]] <= 0):
                take_action(action)
                actions_taken.add(vital)
                continue

        # Check and stabilize
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue
        elif vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # Examine Airway
            continue
        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue
        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue
        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)
            continue
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()