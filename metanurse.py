while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and sats < 65 or (map_value is not None and map_alue < 20):
        print(17)  # StartChestCompression
        continue

    if events[3] <= 0.1:  # AirwayClear has low relevance
        if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
            print(31)  # UseYankeurSucionCatheter to manage obstruction
        else:
            print(3)  # ExamineAirway
    elif events[7] > 0.1:  # BreathingNone detected
        print(29)  # UseBagValveMask for assisted breathing
    elif sats is not None and sats < 88:
        print(30)  # UseNonRebreatherMask to increase oxygen
    elif map_value is not None and map_value < 60:
        print(15)  # GiveFluids to improve circulation
    elif resp_rate is not None and resp_rate < 8:
        print(4)  # ExamineBreathing
    else:
        conditions_met = (
            sats is not None and sats >= 88 and
            map_value is not None and map_value >= 60 and
            resp_rate is not None and resp_rate >= 8 and
            events[3] > 0.1  # Airway not blocked
        )
        if conditions_met:
            print(48)  # Finish - John is stabilized
            break
        else:
            print(0)  # DoNothing as a default when no immediate intervention is needed