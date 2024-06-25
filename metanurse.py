while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Critical Conditions Check
    if sats is not None and sats < 65 or map_value is not None and map_value < 20:
        print(17)  # Start Chest Compression
        continue

    # Establish Airway
    airway_clear = events[3] > 0.1  # Check if airway events indicate clarity
    if not airway_clear:
        print(3)  # Examine Airway
        continue

    # Manage Breathing Issues
    if events[7] > 0.1:  # BreathingNone significant relevance
        print(29)  # Use Bag Valve Mask
        continue

    # Check and Manage Sats for Breathing
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Check and Manage Circulation
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # If Respiratory Rate is Too Low
    if resp_rate is not None and resp_rate < 8:
        print(4)  # Examine Breathing
        continue

    # Check if all essentials are stable
    if (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map_value >= 60
        and resp_rate is not None
        and resp_rate >= 8
    ):
        print(48)  # Finish Scenario
        break

    print(0)  # Continue Monitoring