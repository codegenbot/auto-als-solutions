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
    if events[3] == 0:  # No indication that AirwayClear was recently observed
        print(3)  # ExamineAirway
        continue

    # B - Breathing
    if (events[7] > 0.1) or (
        resp_rate is not None and resp_rate < 8
    ):  # BreathingNone or low respiration rate
        print(4)  # ExamineBreathing
        continue

    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # C - Circulation
    if map_value is None or (map_value is not None and map_value < 60):
        print(5)  # ExamineCirculation
        continue

    # D - Disability
    if events[22] == 0:  # AVPU_U indicating unresponsiveness
        print(8)  # ExamineResponse
        continue

    # E - Exposure
    if (
        events[26] == 0 or events[27] == 0
    ):  # ExposurePeripherallyShutdown or ExposureStainedUnderwear not recently observed
        print(7)  # ExamineExposure
        continue

    # Update and maintain vital measurements
    if times[5] == 0:
        print(25)  # UseSatsProbe
        continue

    if map_value is not None and map_value < 70:
        print(15)  # GiveFluids
        continue

    # If patient seems stable, finish the scenario
    if sats is not None and resp_rate is not None and map_value is not None:
        if sats >= 88 and map_value >= 60 and resp_rate >= 8:
            print(48)  # Finish
            break

    # Default action if no other conditions are met
    print(0)  # DoNothing