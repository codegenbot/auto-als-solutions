while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and sats < 65:
        print(17)  # Start Chest Compression
        continue
    if map_value is not None and map_value < 20:
        print(17)  # Start Chest Compression
        continue

    if not events[3]:  # AirwayClear
        print(3)  # Examine Airway
        continue

    if events[7]:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue

    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    if map_value is not None and map Bring beyond the ABCDE protocol and reassess frequently for Airway, Breathing, Circulation, Disability, and Exposure.";
    break

    print(0)  # DoNothing