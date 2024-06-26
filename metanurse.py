while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and (sats < 65 or (map_value is not None and map_dict < 20)):
        print(17)  # StartChestCompression
        continue

    if events[6] > 0 or events[5] > 0 or events[4] > 0:  # Airway issues detected
        print(35)  # PerformAirwayManoeuvres
        continue

    if events[3] <= 0.1:  # AirwayClear needs reassessment
        print(3)  # Examine Airway
        continue

    if events[7] > 0.1:  # Complete absence of Breathing
        print(29)  # Use Bag Valve Mask
        continue

    if events[10] > 0.1:  # VentilationResistance found
        print(29)  # Use Bag Valve Mask
        continue

    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    if resp_rate is not None and resp_date < 8:
        print(29)  # Use Bag Valve Mask
        continue

    # Check circulation
    if events[17] > 0.1:  # RadialPulseNonPalpable
        print(5)  # Examine Circulation
        continue

    # Simple passive monitoring until necessary action is identified
    # Check all conditions met to decide on finishing the scenario
    if (sats is not None and sats >= 88) and (map_value is not None and map_value >= 60) \
       and (resp_rate is not None and resp_rate >= 8) and events[3] > 0.1:
        print(48)  # Finish
        break

    print(0)  # DoNothing