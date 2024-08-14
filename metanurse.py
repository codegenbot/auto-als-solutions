import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        sys.stdout.flush()
        if action == 48:
            done = True

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )

        vitals = {
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"],
                    vital_signs_values,
                )
            )
        }

        # Examining Airway
        if any(events[idx] > 0 for idx in [3, 4, 5, 6, 7]):
            if events[7] > 0:
                take_action(29)  # Use Bag Valve Mask if breathing is insufficient
            elif events[4] > 0:
                take_action(31)  # Use Yankeur Suction Catheter for vomit
            elif events[6] > 0:
                take_action(36)  # Head Tilt Chin Lift if tongue obstructing
            continue
        
        # Examining Breathing
        if any(events[idx] > 0 for idx in [8, 9, 10, 11, 12, 13, 14]):
            if events[8] > 0:
                take_action(29)  # Use Bag Valve Mask if no breathing
            elif events[13] > 0:
                take_action(30)  # Use Non-Rebreather Mask for low oxygen
            continue
        
        # Examining Circulation
        if any(events[idx] > 0 for idx in [15, 16, 17, 18, 19, 30, 31, 32, 33, 34, 35, 36, 37, 38]):
            if vitals["MAP"] is not None and vitals["MAP"] < 60:
                take_action(15)  # Give Fluids for hypotension

            if vitals["MAP"] is not None and vitals["MAP"] < 20:
                take_action(17)  # Start Chest Compressions

            if vitals["Sats"] is not None and vitals["Sats"] < 65:
                take_action(22)  # Bag During CPR
            continue

        if any(events[idx] > 0 for idx in [20, 21, 22, 23, 24]):
            take_action(6)  # Examine Disability
            continue

        if any(events[idx] > 0 for idx in [25, 26, 27, 28]):
            take_action(7)  # Examine Exposure
            continue

        if 25 not in actions_taken:
            take_action(25)  # Use Sats Probe
            continue
        if 27 not in actions_taken:
            take_action(27)  # Use Blood Pressure Cuff
            continue
        if 16 not in actions_taken:
            take_action(16)  # View Monitor
            continue
        if 3 not in actions_taken:
            take_action(3)  # Examine Airway
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
            take_action(48)
            return

stabilize()