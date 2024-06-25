while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        # Cardiac arrest scenario
        if (sats is not None and sats < 65) or (
            map_value is not None and map_value < 20
        ):
            print(17)  # Start Chest Compression
            continue

        # Check if breathing has ceased
        if (
            events[7] > 0.1
        ):  # BreathingNone is significant, act even if previously checked airway
            print(29)  # Use Bag Valve Mask
            continue

        # Airway check
        if events[3] <= 0.1:
            print(3)  # Examine Airway
            continue

        # Respond to inadequate oxygen saturation
        if sats is not None and sats < 88:
            print(30)  # Use Non Rebreather Mask
            continue

        # Respond to low MAP
        if map_value is not None and map_value < 60:
            print(15)  # Give Fluids
            continue

        # Respond to insufficient respiratory rate
        if resp_rate is not None and resp_rate < 8:
            print(29)  # Use Bag Valve Mask
            continue

        # Regular checks if no immediate actions are necessary
        if times[0] == 0:
            print(3)  # Examine Airway
        elif times[5] == 0:
            print(25)  # Use Sats Probe
        elif times[4] == 0:
            print(38)  # Take Blood Pressure
        else:
            if (
                sats is not None
                and sats >= 88
                and map_value is not None
                and map_value >= 60
                and resp_rate is not None
                and resp_rate >= 8
            ):
                print(48)  # Finish
                break
            else:
                print(0)  # Do Nothing

    except EOFError:
        break