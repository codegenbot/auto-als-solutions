airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False
disability_assessed = False
exposure_assessed = False

while True:
    try:
        # Parse and organize input data
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        # Extract vital signs if measured
        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        # Critical conditions check
        if (sats is not None and sats < 65) or (
            map_value is not None and map_value < 20
        ):
            print(17)  # Start Chest Compression
            continue

        # Airway management
        if not airway_checked or events[3] <= 0.1:
            if events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
                print(31)  # Use Yankeur Suction Catheter
            else:
                print(3)  # Examine Airway
            airway_checked = True
            airway_clear = events[3] > 0.1
            continue

        # Breathing management
        if not breathing_assessed:
            if events[7] > 0.1:  # BreathingNone
                print(29)  # Use Bag Valve Mask
                continue
            else:
                print(4)  # Examine Breathing
            breathing_assessed = True
            continue

        # Circulation management
        if airway_clear and not circulation_assessed:
            print(5)  # Examine Circulation
            circulation_assessed = True
            continue

        # Disability (neurological status)
        if not disability_assessed:
            print(6)  # Examine Disability
            disability_assessed = True
            continue

        # Case of Exposure and Completion Check
        if (
            airway_clear
            and breathing_assessed
            and circulation_assessed
            and disability_assessed
        ):
            if not exposure_assessed:
                print(7)  # Examine Exposure
                exposure_assessed = True
                continue

            # Check if all conditions are stabilised
            all_stable = all(
                [
                    airway_clear,
                    sats is not None and sats >= 88,
                    map_value is not None and map_value >= 60,
                    resp_rate is not None and resp_rate >= 8,
                ]
            )

            if all_stable:
                print(48)  # Finish
                break

        print(0)  # Do Nothing

    except EOFError:
        break