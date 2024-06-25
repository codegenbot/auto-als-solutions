while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Check for immediate life threats
    if sats is not None and (sats < 65 or (map_value is not None and map_value < 20)):
        print(17)  # Start Chest Compression
        continue

    # A - Airway
    if events[3] <= 0.049:  # No recent relevant airway check
        print(3)  # Exoke Airway
        continue

    # B - Breathing
    if events[7] > 0.049:  # Breathing issues observed
        print(29)  # Use Bag Valve Mask
        continue

    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # C - Circulation
    if map_value is not None and map_value < 60:
        print(5)  # Examine Circulation
        continue
    if all(t > 0.049 for t in times[:7]):  # If no recent measurements
        print(16)  # View Monitor
        continue

    # D - Disability
    if (
        events[21] > 0.049 or events[22] > 0.049
    ):  # Decreasing consciousness (AVPU U or V)
        print(6)  # ExamineDisability
        continue

    # E - Exposure
    if events[26] > 0.049 or events[27] > 0.049:  # Critical exposure conditions
        print(7)  # Examine Exposure
        continue

    # If all critical conditions are met
    if sats is not None and map_value is not None and resp_rate is not None:
        if sats >= 88 and map_value >= 60 and resp_rate >= 8:
            print(48)  # Finish
            break

    # Default action if no critical action is required
    print(0)  # DoNothing