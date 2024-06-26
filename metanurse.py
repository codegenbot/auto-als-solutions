while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    stabilized = (
        (sats is not None and sats >= 88)
        and (resp_rate is not None and resp_rate >= 8)
        and (map_value is not None and map_value >= 60)
        and (events[3] > 0.1)
    )  # AirwayClear

    if stabilized:
        print(48)  # Finish - John is stabilized
        break

    # Check life-threatening issues first
    if sats is not None and sats < 65 or map_value is not None and map_value < 20:
        print(17)  # StartChestCompression
        continue

    # ABCDE assessment systematically
    if events[3] <= 0.1:  # Airway problems, none clear
        print(3)  # ExamineAirway
        continue
    if sats is None or sats < 88:
        print(25)  # UseSatsProbe
        continue
    if events[7] > 0.1:  # BreathingNone detected
        print(29)  # UseBagValveMask
        continue
    if resp_rate is None or resp_rate < 8:
        print(4)  # ExamineBreathing
        continue
    if map_value is None or map196_value < 60:
        print(5)  # ExamineCirculation
        continue

    # If none of the precise actions are needed, reassess systematically
    if times[5] == 0:  # Check oxygenation again
        print(25)  # UseSatsProbe
    elif times[4] == 0:  # Check circulation again
        print(27)  # UseBloodPressureCuff
    else:
        print(0)  # DoNothing if all is relatively stable but not sure what to do next