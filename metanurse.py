actions_taken = set()
while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate Critical Handling
    if (sats is not None and sats < 65) or (
        map_value is not None and map_event_value < 20
    ):
        print(17)  # StartChestCompression
        break

    # Airway assessment first
    if 3 not in actions_taken:
        print(3)  # ExamineAirway
        actions_taken.add(3)
        continue

    # Check whether airway intervention needed
    if events[7] > 0.1:  # BreathingNone
        print(32)  # UseGuedelAirway
        continue

    # Circulation check if pulse non palpable
    if 5 not in actions_taken:
        print(5)  # ExamineCirculation
        actions_taken.add(5)
        continue

    # If pulse non-palpable, apply interventions and monitor
    if events[17] > 0.1:  # RadialPulseNonPalpable
        if 15 not in actions_taken:
            print(15)  # GiveFluids
            actions_taken.add(15)
            continue
        if 38 not in actions_taken:
            print(38)  # TakeBloodPressure
            actions_taken.add(38)
            continue

    # Breathing interventions if needed
    if resp_rate is not None and resp_rate < 8:
        if 29 not in actions_taken:
            print(29)  # UseBagValveMask
            actions_taken.add(29)
            continue

    # Check saturation and assist breathing
    if sats is not None and sats < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Handle Disability if needed
    if 6 not in actions_taken and events[22] <= 0.1:  # AVPU_U has low relevance
        print(6)  # ExamineDisability
        actions_taken.add(6)
        continue

    # Stabilization completeness check
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
        print(0)  # DoNothing when no immediate intervention is needed