import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    
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

        # Check for cardiac arrest conditions
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # Start chest compressions
            continue

        # Stabilize vital signs
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        # Check and Treat cardiac arrhythmias
        significant_heart_rhythm_events = [31, 32, 33, 34, 35, 36, 37]
        if any(events[i] > 0 for i in significant_heart_rhythm_events):
            take_action(2)  # Check Rhythm
            continue

        # Ensure measurements tools are used
        if 27 not in actions_taken:
            actions_taken.add(27)
            take_action(27)  # Use Blood Pressure Cuff
            continue
        if 25 not in actions_taken:
            actions_taken.add(25)
            take_action(25)  # Use Sats Probe
            continue
        if 16 not in actions_taken:
            actions_taken.add(16)
            take_action(16)  # View Monitor
            continue
        if 38 not in actions_taken:
            actions_taken.add(38)
            take_action(38)  # Take Blood Pressure
            continue

        # Perform ABCDE assessments
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # Examine Airway
            continue
        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # Examine Breathing
            continue
        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # Examine Circulation
            continue
        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)  # Examine Disability
            continue
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # Examine Exposure
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()