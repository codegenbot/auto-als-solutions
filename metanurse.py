while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        # If no recent measurement, treat as None
        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        # Critical Conditions Check for immediate actions
        if sats is not None and sats < 65 or map_value is not None and map_status < 20:
            print(17)  # Start Chest Compression
            continue

        # Examine Airway
        if not events[3]:  # AirwayClear event not present
            print(3)  # Examine Airway
            continue

        # Manage Breathing Issues
        if events[7]:  # BreathingNone significant relevance
            print(29)  # Use Bag Valve Mask
            continue

        # Ensure oxygen saturation levels are sufficient
        if sats is not None and sats < 88:
            print(30)  # Use Non Rebreather Mask
            continue

        # Address Circulatory concerns
        if map_value is not None and map_value < 60:
            print(15)  # Give Fluids
            continue

        # Ensure Adequate Respiratory Rate
        if resp_rate is not None and resp_rate < 8:
            print(4)  # Examine Breathing
            continue

        # Verify all essential parameters are within required range to finish
        if sats is not None and sats >= 88 and map_value is not None and map_value >= 60 and resp_rate is not None and resp_rate >= 8:
            print(48)  # Finish scenario
            break
        else:
            print(0)  # DoNothing if not all parameters are stable
            continue

    except Exception:
        break