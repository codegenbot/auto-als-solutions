import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()

    for _ in range(350):
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

        # Check for cardiac arrest
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # Start chest compressions
            continue

        # Ensure required tools are used
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

        # Stabilize oxygen saturation
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        # Stabilize respiratory rate
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        # Stabilize mean arterial pressure
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        # Check and treat cardiac arrhythmias
        unstable_rhythms = [27, 28, 29, 32]  # Include significant rhythms indicating instability
        if any(events[i] > 0 for i in unstable_rhythms):
            take_action(24)  # Use Monitor Pads for cardioversion
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:  # Assume tachyarrhythmia threshold
            take_action(9)  # Give Adenosine if over 150 bpm
            continue

        arrhythmias_needing_attention = [26, 30, 31]  # Paced or less critical rhythms
        if any(events[i] > 0 for i in arrhythmias_needing_attention):
            take_action(2)  # Check Rhythm 
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

        # Confirm patient stability and finish if stabilized
        if (vitals["Sats"] is not None and vitals["Sats"] >= 88 and
           vitals["RR"] is not None and vitals["RR"] >= 8 and
           vitals["MAP"] is not None and vitals["MAP"] >= 60):
            take_action(48)  # Finish
            break

        take_action(0)  # DoNothing if no action is necessary

if __name__ == "__main__":
    stabilize()