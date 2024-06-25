while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    heart_rate = measurements[0] if times[0] > 0 else None

    # Critical Conditions Check
    if sats is not None and sats < 65 or map_value is not None and map_value < 20:
        print(17)  # Start Chest Compression
        continue

    # Re-check Rhythm when critical values are observed
    if sats is not None and sats < 88 or map_value is not None and map_value < 60:
        print(2)  # Check Rhythm
        continue

    # Manage airway
    if events[3] <= 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
        print(3)  # Examine Airway
        continue

    # Resolve breathing problems
    if events[7] > 0.1:  # BreathingNone significant relevance
        print(29)  # Use Bag Valve Mask
        continue

    # Emergency interventions
    if heart_rate is not None and heart_rate < 30:
        print(10)  # Give Adrenaline
        continue

    # Manage Breathing
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Manage Circulation
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Disability and consciousness checks
    if events[22] > 0.1 or events[23] > 0.1:  # Unresponsive or worse
        print(6)  # Examine Disability
        continue

    # Exposure check for additional symptoms
    if events[26] > 0.1 or events[27] > 0.1:
        print(7)  # Examine Exposure
        continue

    # If all essentials are stable, finish
    if sats is not None and sats >= 88 and map_value is not None and map_value >= 60 and resp_rate is not None and resp_rate >= 8:
        print(48)  # Finish Scenario
        break

    print(0)  # DoNothing, continue monitoring