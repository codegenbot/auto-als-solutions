while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate life-threatening checks
    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        print(17)  # StartChestCompression
        continue

    # ABCDE Examination Sequence
    if events[3] <= 0.1:  # AirwayClear has low relevance or unknown
        print(3)  # ExamineAirway
    elif resp_rate is not None and resp_rate < 8:
        print(4)  # ExamineBreathing for detailed assessment
    elif map_value is None or map_value < 60:
        print(27)  # Use Blood Pressure Cuff for MAP check
        print(5)  # ExamineCirculation
    elif sats is not None and sats < 88:
        print(30)  # UseNonRebreatherMask
    elif (
        (sats is None or sats >= 88)
        and (map_value is None or map_value > 60)
        and (resp_rate is None or resp_rate >= 8)
    ):
        print(48)  # Finish - Assume John is stabilized
        break
    else:
        print(0)  # DoNothing currently no immediate intervention identified