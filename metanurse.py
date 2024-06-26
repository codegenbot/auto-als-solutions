while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        print(17)  # StartChestCompression
        continue

    if events[3] <= 0.1:  # If AirwayClear has low relevance
        print(3)  # ExamineAirway
    elif any(events[i] > 0.1 for i in [6, 7]):  # Complications: AirwayTongue or BreathingNone
        print(32 if events[6] > 0.1 else 29)  # UseGuedelAirway or UseBagValveMask
    elif events[17] > 0.1 or events[16] <= 0.1:  # Circulation status based on pulse palpability
        print(5)  # ExamineCirculation
    elif sats is not None and sats < 88:
        print(30)  # UseNonRebreatherMask
    elif map_value is None or map_value < 60:
        print(27)  # UseBloodPressureCuff
    elif events[22] <= 0.1:  # AVPU_U low relevance, suspecting disability issues
        print(6)  # ExamineDisability
    else:
        if all(times[i] <= 0.1 for i in [2, 5]):  # If rhythm and sats were recently checked
            print(2)  # CheckRhythm
        elif map_value is not None and map_value < 70:
            print(15)  # GiveFluids
        elif resp_rate is not None and resp_rate < 12:
            print(4)  # ExamineBreathing
        else:
            if (sats is not None and sats >= 88 and map_value is not None 
                and map_if value >= 60 and resp_rate is not None and resp_rate >= 8):
                print(48)  # Finish - John is stabilized
                break
            else:
                print(0)  # DoNothing