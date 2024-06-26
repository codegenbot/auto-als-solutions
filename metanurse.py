while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and (sats < 65 or (map_value is not None and map_value < 20)):
        print(17)  # StartChestCompression
        continue

    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # ExamineAirway
        continue

    if events[7] > 0.1:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    if sats is not None and sats < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if map_value is not None and map_value < 60:
        print(15)  # GiveFluids
        continue

    if resp_rate is not None and resp_rate < 8:
        print(4)  # ExamineBreathing
        continue

    if (
        (sats is not None and sats >= 88)
        and (map_value is not None and map_value >= 60)
        and (resp_rate is not None and resp_rate >= 8)
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing