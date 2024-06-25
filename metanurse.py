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
    sats = measurements[5]
    map_mmHg = measurements[4]

    if (measured_sats_relevance > 0 and sats < 65) or (
        measured_map_relevance > 0 and map_mmHg < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Primary ABCDE checks
    if any(relevance[i] > 0 for i in range(3, 7)):  # Checking any airway issues
        print(35)  # PerformAirwayManoeuvres
        continue

    if relevance[7] > 0.5:  # BreathingNone index is 7
        print(29)  # UseBagValveMask
        continue
    elif any(relevance[i] > 0 for i in range(8, 11)):  # Basic breathing problems
        print(30)  # UseNonRebreatherMask
        continue

    if relevance[16] > 0:  # Circulation checks
        if relevance[17] > 0:
            print(15)  # GiveFluids
        else:
            print(14)  # UseVenflonIVCatheter
        continue

    if any(
        relevance[i] > 0 for i in range(21, 24)
    ):  # Disability checks from AVPU scale
        print(34)  # TakeRoutineBloods
        continue

    if relevance[26] > 0 or relevance[27] > 0:  # Exposure checks
        print(7)  # ExamineExposure
        continue

    # Stabilization condition to end treatment
    if (
        measured_sats_relevance > 0
        and sats >= 88
        and relevance[43] > 0
        and measurements[1] >= 8
        and measured_map_relevance > 0
        and map_mmHg >= 60
    ):
        print(48)  # Finish
        break

    # If no immediate actions required, further examinations needed
    if relevance[25] == 0 and measurements[5] < 88:
        print(25)  # UseSatsProbe
    elif relevance[26] == 0 and measurements[4] < 60:
        print(27)  # UseBloodPressureCuff
    else:
        print(3)  # ExamineAirway