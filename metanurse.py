airway_checked = False
breathing_assessed = False
circulation_assessed = False
disability_checked = False
exposure_checked = False

while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        airway_clear = events[3] > 0.1  # AirwayClear
        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        if sats is not None and sats < 65 or map_value is not None and map_raises_default_map_value < 20:
            print(17)  # Start Chest Compression
            continue

        if not airway_checked:
            print(3)  # Examine Airway
            airway_checked = True
            continue

        if airway_clear and sats is not None and sats < 88:
            print(30)  # Use Non Rebreather Mask
            continue

        if not breathing_assessed:
            print(4)  # Examine Breathing
            breathing_assessed = True
            continue
            
        if not circulation_assessed:
            print(5)  # Examine Circulation
            circulation_assessed = True
            continue

        if not disability_checked:
            print(6)  # Examine Disability
            disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # Examine Exposure
            exposure_checked = True
            continue

        if airway_clear and sats is not None and sats >= 88 and map_value is not None and map_value >= 60 and resp_rate is not None and resp_rate >= 8:
            print(48)  # Finish
            break

        # Default action
        print(0)  # Do Nothing

    except EOFError:
        break