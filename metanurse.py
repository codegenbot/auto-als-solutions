import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    
    def need_examine(event_indices):
        return any(events[i] > 0 for i in event_indices)
    
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
            take_action(17)  # Start chest compressions immediately
            continue

        if vitals["MAP"] is None:
            take_action(27)  # Use blood pressure cuff
            continue
        if vitals["Sats"] is None:
            take_action(25)  # Use sats probe
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag-valve mask
            continue

        if need_examine(range(3, 7)):
            take_action(3)  # Examine airway
            continue

        if need_examine(range(7, 15)):
            take_action(4)  # Examine breathing
            continue

        if need_examine(range(15, 20)):
            take_action(5)  # Examine circulation
            continue

        if need_examine(range(20, 26)):
            take_action(6)  # Examine disability
            continue

        if need_examine(range(26, 33)):
            take_action(7)  # Examine exposure
            continue

        take_action(48)  # Finish action
        break

if __name__ == "__main__":
    stabilize()