airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False
stabilise_attempted = False

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

        if not airway_checked or (events[3] <= 0.1 and not airway_clear):
            print(3)  # Examine Airway
            airway_checked = True
            airway_clear = events[3] > 0.1
            continue

        if airway_clear and not breathing_assessed:
            print(4)  # Examine Breathing
            breathing_assessed = True
            if events[7] > 0.1:  # BreathingNone
                print(29)  # Use Bag Valve Mask
                continue
            elif sats is not None and sats < 88:
                print(30)  # Use Non Rebreather Mask
                continue

        if airway_clear and breathing_assessed and not circulation_assessed:
            print(5)  # Examine Circulation
            circulation_assessed = True
            if map_value is not None and map_value < 60 or events[17] > 0.1:  # RadialPulseNonPalpable
                print(15)  # Give Fluids
                continue

        all_stable = all(
            [
                airway_checked,
                breathing_assessed,
                circulation_assessed,
                sats is not None and sats >= 88,
                map_value is not None and map_value >= 60,
                resp_rate is not None and resp_rate >= 8,
            ]
        )

        if all_stable and not stabilise_attempted:
            stabilise_attempted = True
            print(6)  # Examine Disability

        elif all_stable:
            print(48)  # Finish
            break

        print(0)  # Do Nothing in absence of direct action or new information

    except EOFRed:
        break