while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate critical condition check
    if sats is not None and sats < 65 or map_value is not None and map_pvalue < 20:
        print(17)  # Start Chest Compression
        continue

    # Sequential ABCDE assessment with necessary interventions
    # A - Airway Management
    if events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
        print(36)  # PerformHeadTiltChinLift
        continue

    # B - Breathing Management
    if events[7] > 0.1:
        print(29)  # Use Bag Valve Mask
        continue

    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue
    
    # C - Circulation Management
    if not any(events[28:34]):  # Check if abnormal rhythms detected
        print(2)  # Check Rhythm
        continue

    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # D - Disability Assessment
    if events[21] > 0.1 or events[22] > 0.1:
        print(6)  # Examine Disability
        continue

    # Stability Check
    if (
        sats is not None and sats >= 88
        and map_value is not None and map_value >= 60
        and resp_rate is not None and resp_rate >= 8
    ):
        print(48)  # Finish
        break

    print(0)  # Default action if none above conditions met