while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    # Vital signs check based on the measurement times
    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    heart_rate = measurements[0] if times[0] > 0 else None

    # Critical conditions check
    if sats is not None and sats < 65:
        print(17)  # StartChestCompression
        continue

    if map_value is not None and map_value < 20:
        print(17)  # StartChestCompression
        continue

    # ABCDE Protocol Sequence Execution
    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # ExamineAirway
        continue

    if events[7] > 0.1:  # BreathingNone
        if events[17] > 0.1:  # RadialPulseNonPalpable
            print(17)  # StartChestCompression
        else:
            print(29)  # UseBagValveMask
        continue

    if sats is not None and sats < 88:
        if events[14] > 0.1:  # BreathingPneumothoraxSymptoms
            print(5)  # ExamineBreathingFix issue with tension pneumothorax
        else:
            print(30)  # UseNonRebreatherMask
        continue

    if map_value is not None:
        if map_value < 60:
            print(15)  # GiveFluids
        elif heart_rate is not None and (heart_rate < 60 or heart_rate > 100):
            print(5)  # ExamineCirculation - possibly adjust heart rate or give drugs
        else:
            print(4)  # ExamineBreathing - more detailed breathing assessment
        continue

    if resp_rate is not None and resp_rate < 8:
        print(4)  # ExamineBreathing
        continue

    # Check for Stability to Finish
    if (
        (sats is not None and sats >= 88)
        and (map_value is not None and map_value >= 60)
        and (resp_rate is not None and respate >= 8)
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing or adjust the default action