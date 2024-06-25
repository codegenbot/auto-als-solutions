while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate Response to Critical Conditions
    if sats is not None and sats < 65 or map_value is not None and map_value < 20:
        print(17)  # Start Chest Compression
        continue

    # Airway Management
    if events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
        print(31)  # Use Yankeur Suction Catheter to clear obstruction
        continue
    else:
        print(3)  # Examine Airway
        continue

    # Breathing Assessment
    if events[7] > 0.1:  # BreathingNone significant
        print(29)  # Use Bag Valve Mask
        continue

    # Circulation Check
    if events[32] > 0.1 or events[38] > 0.1:  # Dangerous heart rhythms
        print(28)  # AttachDefibPads
        continue
    elif events[18] <= 0.1:  # Implication of no muffled heart sounds (normal)
        print(5)  # Examine Circulation
        continue

    # Stabilizing Measures
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Ongoing Monitoring and Responsive Actions
    print(2)  # Check Rhythm if no normal heart rate is detected

    # Check for Stability
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

    print(0)  # DoNothing, continue monitoring