import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    
    # Initial checks
    initial_checks = [27, 25]  # Blood Pressure Cuff, Sats Probe

    for check in initial_checks:
        take_action(check)
        actions_taken.add(check)

    for step in range(350):
        observations = list(map(float, input().strip().split()))

        # Check if we received the correct number of observations
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        # Split the observations into the relevant sections
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        # Parse vital signs
        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Perform necessary measurements if values are missing
        if vitals["MAP"] is None and 27 not in actions_taken:
            take_action(27)  # UseBloodPressureCuff
            actions_taken.add(27)
            continue
        
        if vitals["Sats"] is None and 25 not in actions_taken:
            take_action(25)  # UseSatsProbe
            actions_taken.add(25)
            continue

        if (vitals["MAP"] is None or vitals["Sats"] is None) and 16 not in actions_taken:
            take_action(16)  # ViewMonitor
            actions_taken.add(16)
            continue

        # Check vital signs for critical conditions
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        # Stabilization actions
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        # Action for suspected unstable tachyarrhythmia
        if vitals["HR"] is not None and vitals["HR"] > 150:
            take_action(24)  # Use Monitor Pads
            continue

        # ABCDE examination sequence
        examine_order = [3, 4, 5, 6, 7, 8]
        for action in examine_order:
            if action not in actions_taken:
                take_action(action)
                actions_taken.add(action)
                break
        else:
            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()