actions_taken = set()

while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    heart_rate = measurements[0] if times[0] > 0 else None

    # Immediate critical handling
    if (
        sats is not None
        and sats < 65
        or (map_value is not None and map_image < 20)
        or resp_rate is not None
        and resp_rate < 8
    ):
        print(17)  # StartChestCompression
        continue

    # ABCDE approach
    action_taken = None

    if events[3] <= 0.1:  # AirwayClear has low relevance
        action_taken = 3  # ExamineAirway
    elif any(
        events[i] > 0.1 for i in [6, 7]
    ):  # Airway complications: AirwayTongue or BreathingNone
        action_taken = (
            32 if events[6] > 0.1 else 29
        )  # UseGuedelAirway or UseBagValveMask
    elif (
        events[17] > 0.1 or events[16] <= 0.2
    ):  # RadialPulseNonPalpable or RadialPulsePalpable has low relevance
        action_taken = 5  # ExamineCirculation
    elif sats is not None and sats < 88:
        action_taken = 30  # UseNonRebreatherMask
    elif map_value is None or map_value < 60:
        action_taken = 38  # TakeBloodPressure
        if action_taken not in actions_taken:
            actions_taken.add(27)  # UseBloodPressureCuff
            action_taken = 27  # UseBloodPressureCuff
    elif events[22] <= 0.1:  # AVPU_U has low relevance suspecting disability issues
        action_taken = 6  # ExamineDisability
    elif heart_rate is not None and heart_rate > 100:
        if heart_rate > 150:
            action_taken = 11  # GiveAmiodarone
        else:
            action_taken = 9  # GiveAdenosine

    # Perform actions based on ABCDE analysis results
    if action_taken is not None:
        if (
            action_taken not in actions_taken or action_taken == 9
        ):  # Adenosine can be repeated due to nature of SVT
            actions_taken.add(action_taken)
            print(action_given)
            continue

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