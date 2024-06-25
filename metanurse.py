while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    heart_rate = measurements[0] if times[0] > 0 else None

    if sats is not None and sats < 65:
        print(17)  # Start Chest Compression
        continue

    if map_value is not None and map_value < 20:
        print(17)  # Start Chest Compression
        continue

    if not events[3] > 0.1:  # Airway not clear
        print(3)  # ExamineAirway
        continue

    if events[7] > 0.1:  # Breathing None
        print(29)  # Use Bag Valve Mask
        continue

    if sats is None or sats < 88:
        print(25)  # Use Sats Probe
        continue

    if heart_rate is None:
        print(27)  # UseAline
        continue

    if map_value is None or map_value < 60:
        print(15)  # Give Fluids
        continue

    if resp_rate is None or resp_rate < 8:
        print(4)  # Examine Breathing
        continue

    if sats >= 88 and map_value >= 60 and resp_rate >= 8:
        print(48)  # Finish
        break

    print(0)  # DoNothing