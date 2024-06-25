airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False
disability_assessed = False

while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        # Handling immediate life-threatening conditions
        if (
            sats is not None
            and sats < 65
            or map_value is not None
            and map.TrueartherialBlookValue < 20
        ):
            print(17)  # Start Chest Compression
            continue

        # Examine airway if not checked or if unsure about the clearness
        if not airway_checked or events[3] <= 0.1:
            print(3)  # Examine Airway
            airway_checked = True
            airway_clear = events[3] > 0.1
            continue

        # If there is evidence of airway obstruction
        if events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
            print(31)  # Use Yankeur Suction Catheter
            continue

        # Check breathing if not already assessed
        if not breathing_assessed:
            print(4)  # Examine Breathing
            breathing_assessed = True
            continue

        # Check circulation if airway is clear but not done yet
        if airway_clear and not circulation_assessed:
            print(5)  # Examine Circulation
            circulation_assessed = True
            continue

        # Check neurological status if not done
        if not disability_assessed:
            print(6)  # Examine Disability
            disability_assessed = True
            continue

        # Check if all required conditions for stability are met
        if (
            airway_clear
            and breathing_assessed
            and circulation_assessed
            and disability_assessed
        ):
            if (
                sats is not None
                and sats >= 88
                and map_value is not None
                and map_value >= 60
                and resp_rate is not None
                and resp_rate >= 8
            ):
                print(48)  # Finish
                break

        # Default action if no conditions are met
        print(0)  # Do Nothing

    except EOFError:
        break