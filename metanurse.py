airway_checked = False
airway_clear = False
breathing_assessed = False
breathing_stabilized = False
circulation_assessed = False
disability_checked = False
exposure_checked = False

while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        if (
            sats is not None and sats < 65
            or map_value is not None and map_value < 20
        ):
            print(17)  # Start Chest Compression
            continue

        if not airway_checked or events[3] <= 0.1:
            print(3)  # Examine Airway
            airway_checked = True
            airway_clear = events[3] > 0.1
            continue
        
        if airway_clear and not breathing_assessed:
            print(4)  # Examine Breathing
            breathing_assessed = True
            breathing_stabilized = True if resp_rate is not None and resp_rate >= 8 else False
            continue
        
        if breathing_stabilized and not circulation_assessed:
            print(5)  # Examine Circulation
            circulation_assessed = True
            continue

        if airway_clear and breathing_stabilized and circulation_assessed:
            if sats is not None and sats < 88:
                print(30)  # Use Non Rebreather Mask
            elif map_value is not None and map_value < 60:
                print(15)  # Give Fluids
            elif resp_rate is not None and resp_rate < 8:
                print(29)  # Use Bag Valve Mask
            else:
                print(48)  # Finish
                break

        print(0)  # DoNothing if no condition matched
        
    except EOFError:
        break