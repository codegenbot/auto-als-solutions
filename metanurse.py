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

    # Bring vital tools frequently in use
    if times[5] == 0:  # Sats not measured
        print(25)  # Use Sats Probe
        continue
    if times[4] == 0:  # MAP not measured
        print(27)  # Use Blood Pressure Cuff
        continue

    # Airway management
    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # Examine Airway
        continue

    # Breathing management
    if events[7] > 0.1:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Circulation management
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # If all conditions are met for stabilization
    if (
        (sats is not None and sats >= 88)
        and (map_value is not None and map_value >= 60)
        and (resp_rate is not None and resp_rate >= 8)
    ):
        print(48)  # Finish
        break

    # Examine other systems to get more information
    print(5)  # Examine Circulation