while True:
    observations = input().split()
    relevance = [float(obs) for obs in observations[:53]]
    measurements = [float(obs) for obs in observations[53:]]

    measured_sats_relevance = relevance[52]
    measured_map_relevance = relevance[51]
    sats = measurements[5]
    map_mmHg = measurements[4]

    if (measured_sats_relevance > 0 and sats < 65) or (
        measured_map_relevance > 0 and map_mmHg < 20
    ):
        print(17)  # StartChestCompression
        continue

    if any(relevance[i] > 0 for i in range(3, 7)):  # Checking any airway issues
        print(35)  # PerformAirwayManoeuvres
        continue

    if relevance[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    elif any(relevance[i] > 0 for i in range(8, 11)):  # Other breathing problems
        print(30)  # UseNonRebreatherMask
        continue

    if relevance[16] > 0:  # Circulation checks - Palpable Pulse exists
        if relevance[17] > 0:  # RadialPulseNonPalpable
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

    if relevance[25] == 0 and measurements[5] < 88:
        print(25)  # UseSatsProbe
    elif relevance[26] == 0 and measurements[4] < 60:
        print(27)  # UseBloodPressureCuff
    else:
        print(3)  # ExamineAirway