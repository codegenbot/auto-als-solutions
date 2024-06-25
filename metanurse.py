airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False
disability_assessed = False
exposure_assessed = False

while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            print(17)  # Start Chest Compression
            continue

        if not airway_checked or events[3] == 0:
            print(3)  # Examine Airway
            airway_checked = True
            airway_clear = events[3] > 0
            continue

        if airway_clear and not breathing_assessed:
            print(4)  # Examine Breathing
            breathing_assessed = True
            continue

        if breathing_assessed and not circulation_assessed:
            print(5)  # Examine Circulation
            circulation_assessed = True
            continue

        if circulation_assessed and not disability_assessed:
            print(6)  # Examine Disability
            disability_assessed = True
            continue

        if disability_assessed and not exposure_assessed:
            print(7)  # Examine Exposure
            exposure_assessed = True
            continue

        if (
            airway_clear
            and breathing_assessed
            and circulation_assessed
            and disability_assessed
            and exposure_assessed
        ):
            stabilized = (
                sats is not None
                and sats >= 88
                and map_value is not None
                and map_value >= 60
                and resp_rate is not None
                and resp_rate >= 8
            )
            if stabilized:
                print(48)  # Finish
                break

        print(
            0
        )  # Do Nothing in absence of any direct action based on current knowledge

    except EOFError:
        break