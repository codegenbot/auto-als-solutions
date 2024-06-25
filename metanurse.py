while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Critical Conditions Check for immediate life-threatening indicatives
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        print(17)  # Start Chest Compression
        continue

    # Establish and ensure Airway is clear
    airway_clear = events[3] > 0.1
    if not airway_clear:
        print(3)  # Examine Airway
        continue

    # Manage Breathing: Check if there is no breathing
    if events[7] > 0.1:  # BreathingNone significant relevance
        print(17)  # Start Chest Compression
        continue

    # Oxygen Management
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Circulation Management: If MAP is below adequate levels
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # In case of low respiratory rate, manage appropriately
    if resp_rate is not None and resp_index < 8:
        print(29)  # Use Bag Valve Mask
        continue

    # Check if all stabilization conditions are met
    if (
        (sats is not None and sats >= 88)
        and (map_value is not None and map_value >= 60)
        and (resp_rate is not None and resp_rate >= 8)
    ):
        print(48)  # Finish Scenario
        break

    # If there's no immediate intervention required, continue assessment
    print(0)  # Continue Monitoring