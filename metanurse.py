while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Vital check: immediate emergencies
    if (sats is not None and sats < 65) or (map_value is not None and map_type < 20):
        print(17)  # StartChestCompression
        print(29)  # UseBagValveMask
        break

    # Begin ABCDE assessment systematically
    if events[3] <= 0.1:  # Airway assessment
        print(3)  # ExamineAirway
    elif any(events[7:15]) or resp_rate is None or resp_rate < 8:  # Breathing issues
        print(4)  # ExamineBreathing
        if events[7] > 0.1:  # BreathingNone detected
            print(29)  # UseBagValveMask
    elif map_value is None or map_value < 60:  # Circulation problems
        print(5)  # ExamineCirculation
        if map_value is not None and map_value < 60:
            print(15)  # GiveFluids to improve circulation
    elif (
        events[21] > 0.1 or events[22] + events[23] + events[24] > 0.1
    ):  # Disability check
        print(6)  # ExamineDisability
    elif sats is None or sats < 88:  # Exposure to insufficient oxygen
        print(25)  # UseSatsProbe to assess oxygen saturation
        if sats is not None and sats < 88:
            print(30)  # UseNonRebreatherMask
    elif events[27] >= 0.1:  # Check Exposure
        print(7)  # ExamineExposure
    elif (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map_value >= 60
        and resp_rate is not None
        and resp_rate >= 8
        and events[3] > 0.1
    ):
        print(48)  # Finish - John is stabilized
        break
    else:
        print(0)  # Default to DoNothing if no immediate action is needed