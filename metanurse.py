while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        # Essential vital stats
        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        # Quick checks for critical condition triggers
        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            print(17)  # Start Chest Compression
            continue

        # Checking through ABCDE:
        if events[3] <= 0.1:  # If Airway not confirmed clear
            print(3)  # Examine Airway
            continue

        if events[7] > 0.1:  # If entirely no breathing
            print(29)  # Use Bag Valve Mask
            continue

        # Circulation issues:
        if times[4] == 0 or map_value is not None and map_value < 60:
            print(15)  # Give Fluids
            continue

        # Disability and exposure checks:
        # More conditions can be added based on simulation inputs and requirements

        # If everything okay, finish:
        if (
            all(e > 0 for e in (sats, map_value, resp_rate))
            and sats >= 88
            and map_value >= 60
            and resp_rate >= 8
        ):
            print(48)  # Finish
            break
        else:
            print(0)  # Do Nothing if undecided state

    except EOFError:
        break