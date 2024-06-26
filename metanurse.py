while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate Critical Handling
    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        print(17)  # StartChestCompression
        continue

    # A - Airway
    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # ExamineAirway
        continue

    # B - Breathing
    if events[7] >= 0.1:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if sats is not None and sats < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # C - Circulation
    if events[17] > 0.1:  # RadialPulseNonPalpable
        print(27)  # UseBloodPressureCuff
        print(16)  # ViewMonitor
        continue
    if map_value is not None and map_value < 60:
        print(27)  # UseBloodPressureCuff
        print(16)  # ViewMonitor
        continue
    if events[16] <= 0.1:  # RadialPulsePalpable has low relevance
        print(5)  # ExamineCirculation
        continue

    # D - Disability
    if events[22] <= 0.1:  # AVPU_U has low relevance
        print(6)  # ExamineDisability
        continue

    # E - Exposure
    print(7)  # ExamineExposure

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