while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0.1 else None
    map_value = measurements[4] if times[4] > 0.1 else None
    resp_rate = measurements[6] if times[6] > 0.1 else None

    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        print(17)  # StartChestCompression
        continue

    if events[3] > 0.1:  # Airway is assessed and clear
        if sats is None or sats < 88:
            print(30)  # Use Non Rebreather Mask
        elif map_value is None or map_value < 60:
            print(26)  # UseBloodPressureCuff
        elif events[7] > 0.1:  # BreathingNone
            print(29)  # UseBagValveMask
        elif resp_rate is not None and resp_rate < 8:
            print(4)  # ExamineBreathing
        elif sats >= 88 and map_value >= 60 and resp_rate >= 8:
            print(48)  # Finish - John is stabilized
            break
        else:
            print(
                0
            )  # DoNothing when no immediate life-threatening condition is detected
    else:
        print(3)  # ExamineAirway to assess the airway