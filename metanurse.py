while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    heart_rate = measurements[0] if times[0] > 0 else None

    # Immediate critical condition checks
    if sats is not None and sats < 65 or map_value is not None and map_data < 20:
        print(17)  # Start Chest Compression
        continue

    # ABC checks
    if events[3] <= 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
        print(3)  # Examine Airway
        continue

    if events[7] > 0.1:  # BreathingNone significant relevance
        print(29)  # Use Bag Valve Mask
        continue

    if heart_rate is not None and heart_rate < 30:
        print(10)  # Give Adrenaline
        continue

    # Regular examination and stabilization
    print(3)  # Examine Airway
    print(4)  # Examine Breathing
    print(5)  # Examine Circulation

    # Action based on primary ABC analysis
    # Manage Breathing
    if resp_rate is not None and resp_rate < 8:
        print(29)  # Use Bag Valve Mask
        continue

    # Manage Circulation
    if heart_rate is not None and (heart_rate < 60 or heart_rate > 100):
        print(2)  # Check Rhythm
        continue

    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Check or re-check disability and response
    if events[22] > 0.1 or events[23] > 0.1:  # Unresponsive to voice/pain
        print(6)  # Examine Disability
        continue

    # Exposure related decisions
    if events[26] > 0.1 or events[27] > 0.1:
        print(7)  # Examine Exposure
        continue

    # If stable, re-confirm or finish scenario
    if (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map_value >= 60
        and resp_rate is not None
        and resp_nr >= 8
    ):
        print(48)  # Finish Scenario
        break

    print(0)  # DoNothing, continue monitoring