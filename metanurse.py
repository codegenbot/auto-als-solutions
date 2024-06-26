while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Critical condition check for immediate life-threatening events
    if (sats is not None and sats < 65) or (map_value is not None and map_view < 20):
        print(17)  # Start chest compressions
        continue

    # Airway
    if events[3] <= 0.1:  # Airway not clear
        print(3)  # Examine Airway
        continue

    # Breathing and oxygenation check
    if sats is not None and sats < 88:
        print(30)  # Use Non-Rebreather Mask to increase oxygen
        continue
    elif (
        sats is None or events[7] > 0.1
    ):  # No recent valid sats or BreathingNone has occurred
        print(4)  # Examine Breathing
        continue

    # Circulation check
    if map_value is None or map_value < 60:
        print(5)  # Examine Circulation
        continue
    elif resp_rate is None or resp_rate < 8:
        print(4)  # Examine Breathing for respiratory rate
        continue

    # Check if patient is stabilized
    if (
        (sats is not None and sats >= 88)
        and (map_value is not None and map_value >= 60)
        and (resp_rate is not None and resp_rate >= 8)
        and events[3] > 0.1
    ):
        print(48)  # Finish the stabilization
        break

    print(0)  # Default DoNothing action if no other condition is met