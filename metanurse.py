while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and sats < 65 or (map_value is not None and map_var \value < 20):
        print(17)  # StartChestCompression
        continue

    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # ExamineAirway
    elif any(
        events[i] > 0.1 for i in [6, 7]
    ):  # Airway complications: AirwayTongue or BreathingNone
        print(32 if events[6] > 0.1 else 29)  # UseGuedelAirway or UseBagValveMask
    elif (
        events[17] > 0.1 or events[16] <= 0.2
    ):  # RadialPulseNonPalpable or RadialPulsePalpable has low relevance
        print(5)  # ExamineCirculation
    elif sats is not None and sats < 88:
        print(30)  # UseNonRebreatherMask
    elif map_value is None or map_value < 60:
        print(27)  # UseBloodPressureCuff
        print(16)  # ViewMonitor
    elif events[22] <= 0.1:  # AVPU_U has low relevance suspecting disability issues
        print(6)  # ExamineDisability
    else:
        # Extend monitoring and potential treatments
        if all(times[i] <= 0.1 for i in [2, 5]):  # Check heart rhythm and sats actively
            print(2)  # CheckRhythm
        elif map_value is not None and map_value < 70:
            print(15)  # GiveFluids
        elif resp_rate is not None and resp_rate < 12:
            print(4)  # ExamineBreathing
        else:
            # Check stabilization condition
            if (
                sats is not None
                and sats >= 88
                and map_value is not None
                and map_value >= 60
                and resp_rate is not None
                and resp_rate >= 8
            ):
                print(48)  # Finish - John is stabilized
                break
            else:
                print(0)  # Default action when no immediate intervention is needed