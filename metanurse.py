while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        # Critical Conditions Check for immediate life threats
        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            print(17)  # Start Chest Compression
            continue

        # Examine airway, breathing, and circulation if not examined yet or status unclear
        if events[3] <= 0.1:  # AirwayNotClear
            print(3)  # Examine Airway
            continue

        if any(events[i] <= 0.1 for i in range(6, 9)):  # Breathing issues
            print(4)  # Examine Breathing
            continue

        if events[16] <= 0.1 and events[17] <= 0.1:  # Pulse not palpable
            print(5)  # Examine Circulation
            continue

        # Manage Breathing Issues
        if (events[7] > 0.1 or resp_rate is not None and resp_rate < 8):  # BreathingNone or low rate
            print(29)  # Use Bag Valve Mask
            continue

        # Improve Oxygenation if required
        if sats is not None and sats < 88:
            print(30)  # Use Non Rebreather Mask
            continue

        # Circulation issues management
        if map_value is not None and map_value < 60:
            print(15)  # Give Fluids
            continue

        # If vitals are within safe limits and relatively stable
        if (events[0] > 0.1 and sats is not None and sats >= 88 and
            map_value is not None and map_value >= 60 and
            resp_rate is not None and resp_rate >= 8):
            print(48)  # Finish Scenario
            break
        else:
            print(0)  # Do Nothing, continue monitoring
    except Exception:
        break