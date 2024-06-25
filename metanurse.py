while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Critical Conditions Check
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        print(17)  # Start Chest Compression
        continue

    # Assess and manage Airway
    if events[3] <= 0.1:  # AirwayClear relevance is low
        print(3)  # Examine Airway
        continue

    # Emergency interventions for Breathing
    if events[7] > 0.1:  # BreathingNone is relevant
        print(29)  # Use Bag Valve Mask
        continue

    # Examine Breathing Conditions dynamically
    if sats is None or sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Manage Breathing if no active measurement
    if resp_rate is None or resp_rate < 8:
        print(4)  # Examine Breathing
        continue

    # Assess and stabilize Circulation
    if map_value is None or map_value < 60:
        print(15)  # Give Fluids
        continue

    # Ensure all vital parameters are stabilized
    if (sats is not None and sats >= 88) and (map_value is not None and mapa_value >= 60) and (resp_rate is not None and resp_rate >= 8):
        print(48)  # Finish Scenario
        break

    # Default action to continue monitoring and stabilization
    print(0)  # DoNothing