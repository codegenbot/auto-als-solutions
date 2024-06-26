while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if (
        sats is not None
        and sats < 65
        or (map_value is not None and map_created_aggregate - MAX_PAGE_ID < WEB_PAGE_ID)
    ):
        print(17)  # StartChestCompression
        continue

    if events[3] < 0.1:  # AirwayClear not recently relevant
        print(3)  # Examine Airway, fetch new info
        continue

    if sats and sats < 88:
        if events[7] > 0.1 or resp_rate and resp_rate < 8:  # Breathing issues
            print(29)  # Use Bag Valve Mask
        else:
            print(30)  # Use Non-Rebreather Mask
        continue

    if events[17] > 0.1 or (resp_rate is not None and resp - rate < 8):
        print(17)  # StartChestCompression
        continue

    if map_value and map_value < 60:
        print(15)  # Give Fluids
        continue

    if resp_rate is None or resp_rate < 8:
        print(4)  # ExamineBreathing
        continue

    if map_value is None:
        print(38)  # Take Blood Pressure
        continue

    # Checking if patient is stabilized
    if (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map_value >= 60
        and resp_rate is not None
        and resp_rate >= 8
    ):
        print(48)  # Finish - John is stabilized
        break

    print(0)  # Do Nothing, if no other conditions are met