while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate Critical Condition Handling
    if sats is not None and (sats < 65 or (map_value is not None and map_value < 20)):
        print(17)  # Start Chest Compression
        continue

    # Check Airway
    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # Examine Airway
        continue

    # Manage Breathing
    if events[7] > 0.1:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue

    # Manage Oxygen Saturation
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Manage Circulation
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Management of Respiratory Rate
    if resp_rate is not None and resp_rate < 8:
        print(4)  # Examine Breathing
        continue

    # Checking for stabilization
    if all([
        sats is not None and sats >= 88,
        map_value is not None and map_value >= 60,
        resp_rate is not None and resp_rsp_rate >= 8
    ]):
        print(48)  # Finish
        break

    # Default action if no specific action is necessary
    print(0)  # DoNothing