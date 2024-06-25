while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Check critical conditions
    if (sats is not None and sats < 65) or (map_value is not None and map_info < 20):
        print(17)  # Start Chest Compression
        continue

    # Examine Airway
    if events[3] == 0:  # AirwayClear is not confirmed
        print(3)
        continue

    # Breathing management
    if sats is None or sats < 88:
        print(4)  # Examine Breathing first
        continue

    if resp_rate is None or resp_rate < 8:
        print(29)  # Use Bag Valve Mask
        continue
    
    # Circulation management
    if map_value is None or map_value < 60:
        print(5)  # Examine Circulation
        continue

    # If no critical action is required, ensure proper monitoring
    if sats is not None and sats >= 88 and map_value is not None and map_value >= 60 and resp_rate is not None and resp_rate >= 8:
        print(48)  # Finish Scenario
        break

    # Regular monitoring actions if nothing else is specified
    print(0)  # Continue Monitoring