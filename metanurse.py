import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    initial_checks = [27, 25]  # Attach Blood Pressure Cuff, Sats Probe

    for check in initial_checks:
        take_action(check)
        actions_taken.add(check)

    bp_checked = sats_checked = False

    for step in range(350):
        observations = list(map(float, input().strip().split()))

        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if not bp_checked and 27 in actions_taken:
            take_action(16)  # View Monitor
            bp_checked = True
            continue

        if not sats_checked and 25 in actions_taken:
            take_action(16)  # View Monitor
            sats_checked = True
            continue

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start Chest Compression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:
            if 24 not in actions_taken:
                take_action(24)  # Use Monitor Pads
                actions_taken.add(24)
            else:
                take_action(40)  # DefibrillatorCharge
            continue

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