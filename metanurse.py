while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate Critical Conditions
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        print(17)  # Start Chest Compression
        continue

    # ABCDE assessments
    if events[3] <= 0.1:  # Airway not just cleared or low relevance
        print(3)
    elif events[7] <= 0.1:  # Check Breathing
        print(4)
    elif map_value is None or map_value < 60:  # Circulation - Check or action required
        print(5)  # Examine Circulation
    elif (
        events[23] <= 0.1 or events[24] <= 0.1 or events[25] <= 0.1
    ):  # Check Disability
        print(6)  # Examine Disability
    elif events[26] <= 0.1:  # Exposure not checked
        print(7)  # Examine Exposure
    else:
        # Ensure sufficiency – give necessary aid
        if sats is not None and sats < 88:
            print(30)  # Non-rebreather mask
        elif resp_rate is not None and resp_rate < 8:
            print(29)  # Bag Valve Mask
        else:
            # Check if stabilization criteria are met
            if all(
                [
                    v is not None and v >= thresh
                    for v, thresh in zip([sats, map_value, resp_rate], [88, 60, 8])
                ]
            ):
                print(48)  # Finish - John is stabilized
                break
            else:
                print(0)  # Other actions not critical, do nothing awaiting new data