while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediately handle very critical conditions
    if sats is not None and sats < 65:
        print(17)  # Start Chest Compression
        continue
    
    # Check airway status
    if events[3] <= 0.1:
        print(3)  # Examine Airway
        continue

    # Handle absence of breathing
    if events[7] > 0.1:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue

    # Provide oxygen if saturation is low
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Treat circulatory issues
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Assess breathing if needed
    if resp_rate is None or resp_rate < 8:
        print(4)  # Examine Breathing
        continue

    # Check for stabilization conditions
    if (sats is not None and sats >= 88) and (map_value is not None and map_value >= 60) and (resp_rate is not None and resp_rate >= 8):
        print(48)  # Finish
        break

    # Default action if no other conditions are met
    print(0)  # DoNothing