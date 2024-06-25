while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
            print(17)  # Start Chest Compression
            continue
        
        if events[3] > 0.1:  # AirwayClear
            airway_clear = True
        else:
            airway_clear = False
            print(3)  # Examine Airway
            continue

        if events[7] > 0.1:  # BreathingNone significant
            if events[17] <= 0.1:  # RadialPulseNonPalpable not significant
                print(29)  # Use Bag Valve Mask
            else:
                print(17)  # Start Chest Compression
            continue

        if airway_clear:
            if sats is None or sats < 88:
                print(30)  # Use Non Rebreather Mask
            elif map_value is None or map_value < 60:
                print(15)  # Give Fluids
            elif resp_rate is None or resp_rate < 8:
                print(4)  # Examine Breathing
            else:
                all_stable = (
                    sats is not None
                    and sats >= 88
                    and map_value is not None
                    and map_value >= 60
                    and resp_rate is not None
                    and resp_rate >= 8
                )
                if all_stable:
                    print(48)  # Finish
                    break
                else:
                    print(0)  # Do Nothing
        else:
            print(3)  # Examine Airway

    except EOFError:
        break