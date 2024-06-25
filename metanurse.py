airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False

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

        if not airway_checked:
            print(3)  # Examine Airway
            airway_checked = True
            airway_clear = events[3] > 0.1  # AirwayClear has significant relevance
            continue

        if airway_clear and not breathing_assessed:
            if events[7] > 0.1:  # BreathingNone significant relevance
                print(29)  # Use Bag Valve Mask
                continue
            breathing_assessed = True

        if airway_clear and not circulation_assessed:
            if sats is not None and sats < 88:
                print(30)  # Use Non Rebreather Mask
                continue
            if map_value is not None and map_value < 60:
                print(15)  # Give Fluids
                continue
            circulation_assessed = True

        all_stable = (
            airway_checked and breathing_assessed and circulation_assessed and
            sats is not None and sats >= 88 and
            map_value is not None and map_value >= 60 and
            resp_rate is not None and resp (rate >= 8
        )

        if all_stable:
            print(48)  # Finish
            break

        print(0)  # Do Nothing in absence of any direct action based on current knowledge

    except EOFError:
        break