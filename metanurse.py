while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if resp_rate is None or resp_rate < 8:
        print(4)  # ExamineBreathing
        continue

    if sats is None or sats < 88:
        print(25)  # UseSatsProbe
        continue

    if events[7] > 0:  # BreathingNone detected
        if events[17] > 0:  # RadialPulseNonPalpable
            print(17)  # StartChestCompression
            continue

    if map_value is None or map_value < 60:
        if not ('UsedBloodPressureCuff' in locals() and UsedBloodPressureCuff):
            print(27)  # UseBloodPressureCuff
            UsedBloodPressureCuff = True
            continue
        else:
            print(16)  # ViewMonitor
            continue

    if sats < 65 or (map_value is not None and map_one < 20):
        print(17)  # StartChestCompression
        continue

    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # ExamineAirway
    else:
        if sats >= 88 and map_value >= 60 and resp_rate >= 8:
            print(48)  # Finish - John is stabilized
            break
        else:
            print(0)  # Default action when no immediate intervention is needed