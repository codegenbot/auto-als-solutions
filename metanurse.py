while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            print(17)  # Start Chest Compression
            continue

        # Check if all stable conditions are met
        if (
            sats is not None
            and sats >= 88
            and map_value is not None
            and map_action >= 60
            and resp_rate is not None
            and resp_rate >= 8
        ):
            print(48)  # Finish
            break

        # Examine Measurements and Events
        if sats is not None and sats < 88:
            print(30)  # Use Non Rebreather Mask
        elif map_value is not None and map_value < 60:
            print(15)  # Give Fluids
        elif resp_rate is not None and resp_rate < 8:
            print(4)  # Examine Breathing
        elif events[7] > 0.1:  # BreathingNone has significant relevance
            print(29)  # Use Bag Valve Mask
        elif times[0] == 0:
            print(3)  # Examine Airway
        elif times[5] == 0:
            print(25)  # Use Sats Probe
        elif times[4] == 0:
            print(38)  # Take Blood Pressure
        else:
            print(0)  # Do Nothing if no other conditional matches

    except EOFError:
        break