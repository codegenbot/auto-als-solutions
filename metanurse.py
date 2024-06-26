while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate life-threatening intervention
    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        print(17)  # StartChestCompression
        continue

    # Assess ABCDE systematically
    if events[3] <= 0.1:  # AirwayClear relevance is low, possibly obstructed
        print(3)  # ExamineAirway
    elif events[7] > 0.1 or (resp_rate is not None and resp_rate < 8):
        # BreathingNone is high relevance or bad resp rate, needs intervention
        print(29)  # UseBagValveMask
    elif events[17] > 0.1:  # RadialPulseNonPalpable, indicates circulation issue
        print(17)  # StartChestCompression
    elif sats is not None and sats < 88:
        print(30)  # UseNonRebreatherMask to raise sats
    elif map_value is not None and map_value < 60:
        print(15)  # GiveFluids to raise MAP
    else:
        # Other examinations and interventions based on observations
        if events[5] > 0.1 or events[6] > 0.1 or events[7] > 0.1:
            print(3)  # Recheck Airway if signs of obstruction
        elif events[8] > 0.1:
            print(4)  # Check Breathing thoroughly
        elif events[17] > 0.1 or events[16] <= 0.1:
            print(5)  # Examine Circulation more closely
        elif events[22] > 0.1 or events[23] > 0.1:
            print(6)  # Check Disability (response levels)
        else:
            if (sats is not None and sats >= 88 and
                map_value is not None and map_value >= 60 and
                resp_rate is not None and resp_rate >= 8):
                print(48)  # Finish - John is stabilized
                break
            else:
                print(0)  # Default action when no immediate intervention needed