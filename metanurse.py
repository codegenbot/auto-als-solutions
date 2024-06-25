while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Check for immediate life threats
    if sats is not None and (sats < 65 or (map_value is not None and map_value < 20)):
        print(17)  # Start Chest Compression
        continue

    # A - Airway
    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # Examine Airway
        continue

    # B - Breathing
    if events[7] > 0.1:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue

    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # C - Circulation
    if map_value is not None and map_value < 60:
        print(5)  # Examine Circulation
        continue
    if (
        map_value is not None
        and resp_rate is not None
        and (resp_rate < 8 or resp_rate < 12)
    ):
        print(4)  # Examine Breathing to verify
        continue

    # D - Disability
    if events[22] < 0.1:  # Decreasing AVPU response
        print(8)  # ExamineResponse
        continue

    # E - Exposure
    if events[26] < 0.1 or events[27] < 0.1:  # Check on exposure-related symptoms
        print(7)  # ExamineExposure
        continue

    # Ensure Pulse Oximetry is up to date
    if times[5] < 0.1:
        print(25)  # UseSatsProbe
        continue

    # Ensure proper fluid resuscitation if circulation is compromised
    if map_value is not None and map_value < 70:
        print(15)  # GiveFluids
        continue

    # No immediate actions needed, confirm situation or improve monitoring
    if resp_rate is not None and resp_rate < 12:
        print(4)  # ExamineBreathing
        continue

    # Check stabilization conditions
    if sats is not None and map_value is not None and resp_rate is not None:
        if sats >= 88 and map_value >= 60 and resp- rate >= 8:
            print(48)  # Finish
            break

    # Default check
    print(0)  # DoNothing