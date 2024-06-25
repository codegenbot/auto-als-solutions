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

    # Manage Airway
    if events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
        print(3)  # Examine Airway
        continue

    # Manage Breathing issues
    if events[7] > 0.1:  # BreathingNone significant
        print(29)  # Use Bag Valve Mask
        continue

    # Emergent condition management
    if (
        events[30] > 0.1 or events[37] > 0.1
    ):  # Dangerous heart rhythms, use defib if needed
        print(28)  # AttachDefibPads
        continue

    # Ensure adequate circulation and perfusion
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Use High-Flow Oxygen if breathing is not optimal
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Check Rhythm when abnormal heart rate detected
    if not any(events[28:34]):  # No normal rhythm patterns
        print(2)  # Check Rhythm
        continue

    # Manage Disability - check responsiveness
    if events[21] > 0.1 or events[22] > 0.1:  # AVPU response issues
        print(6)  # Examine Disability
        continue

    # Final check for stabilisation and exit if stable
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