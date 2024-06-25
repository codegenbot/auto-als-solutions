while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and (sats < 65 or (map_value is not None and map_value < 20)):
        print(17)  # Start Chest Compression
        continue

    # Check airway: prioritize if airway concerns evident or not previously cleared
    airway_status = events[3:7]  # AirwayClear, AirwayVomit, AirwayBlood, AirwayTongue
    if any(status > 0 for status in airway_status):
        airway_clear = events[3]  # AirwayClear
        if not airway_clear or max(airway_status[1:]) > airway_clear:
            print(3)  # Examine Airway
            continue

    # Check breathing if no clear distress
    if events[7] > 0.1:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue

    # Oxygen management
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Circulation management
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Check respiration status if falling below critical levels
    if resp_rate is not, and resp_rate < 8:
        print(4)  # Examine Breathing
        continue

    # Final check before finishing: if all vital patient parameters are stable
    if all([
        sats is not None and sats >= 88,
        map_value is not None and map_value >= 60,
        resp_rate is not None and resp_rate >= 8
    ]):
        print(48)  # Finish
        break

    # Default action if no other conditions met
    print(0)  # DoNothing