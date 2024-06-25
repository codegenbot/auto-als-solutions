while True:
    observations = input().split()
    relevance = [
        float(obs) for obs in observations[:46]
    ]  # Including recency of vital sign measurements
    measurements = [
        float(obs) for obs in observations[46:]
    ]  # Actual vital sign measurements

    # Immediate danger conditions
    measured_sats_relevance = relevance[45]
    measured_map_relevance = relevance[44]
    sats = measurements[5] if measured_sats_relevance > 0 else None
    map_mmHg = measurements[4] if measured_map_relevance > 0 else None

    # Handling immediate life-threatening issues
    if sats is not None and sats < 65 or map_mmHg is not None and map_mmHg < 20:
        print(17)  # StartChestCompression
        continue

    # Airway assessment and management
    if relevance[3] > 0 and relevance[7] > 0:  # AirwayObstruction and BreathingNone
        print(31)  # UseYankeurSuctionCatheter
        continue
    elif any(relevance[i] > 0 for i in [3, 4, 5]):  # Check for airway obstruction events
        print(35)  # PerformAirwayManoeuvres
        continue

    # Breathing assessment and management
    if any(relevance[i] > 0 for i in range(7, 11)):
        if relevance[7] > 0:  # BreathingNone
            print(29)  # UseBagValveMask
        elif relevance[9] > 0:  # BreathingSeeSaw, indicating severe difficulty
            print(29)  # UseBagValveMask
        else:
            print(30)  # UseNonRebreatherMask
        continue

    # Circulation checks
    if relevance[16] > 0 or relevance[17] > 0:
        print(15 if relevance[17] > 0 else 14)  # GiveFluids if pulse non-palpable otherwise setup IV
        continue

    # Disability checks from AVPU scale
    if any(relevance[i] > 0 for i in range(21, 24)):
        print(34)  # TakeRoutineBloods
        continue

    # Exposure checks
    if relevance[26] > 0 or relevance[27] > 0:
        print(7)  # ExamineExposure
        continue

    # Regularly check using monitors if values not relevant or recent
    if measured_sats_relevance == 0:
        print(25)  # UseSatsProbe
    elif measured_map_relevance == 0:
        print(27)  # UseBloodPressureCuff
    else: 
        print(3)  # ExamineAirway

    # Stable condition check to end treatment
    if (sats is not None and sats >= 88 and measurements[1] >= 8 and map_mmHg is not None and map_mmHg >= 60):
        print(48)  # Finish
        break