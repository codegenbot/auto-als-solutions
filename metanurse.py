while True:
    observations = input().split()
    relevance = [float(obs) for obs in observations[:53]]
    measurements = [float(obs) for obs in observations[53:]]

    # Check if patient is in immediate danger
    if measurements[5] < 65 or measurements[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Check airway issues
    if relevance[3] > 0 or relevance[4] > 0 or relevance[5] > 0 or relevance[6] > 0:
        print(35)  # PerformAirwayManoeuvres
        continue

    # Check breathing issues
    if relevance[7] > 0 or relevance[8] > 0 or relevance[9] > 0 or relevance[10] > 0:
        if relevance[14] > 0:
            print(29)  # UseBagValveMask
        else:
            print(30)  # UseNonRebreatherMask
        continue

    # Check circulation issues
    if relevance[16] > 0 and relevance[17] > 0:
        print(15)  # GiveFluids
        continue
    elif relevance[17] > 0:
        print(14)  # UseVenflonIVCatheter
        continue

    # Check disability
    if relevance[21] > 0 or relevance[22] > 0 or relevance[23] > 0:
        print(34)  # TakeRoutineBloods
        continue

    # Check exposure issues
    if relevance[26] > 0 or relevance[27] > 0:
        print(7)  # ExamineExposure
        continue

    # Stabilization checks
    if measurements[5] >= 88 and measurements[1] >= 8 and measurements[4] >= 60:
        print(48)  # Finish
        break

    # Default actions to gather more information
    if relevance[25] == 0:
        print(25)  # UseSatsProbe
    elif relevance[26] == 0:
        print(27)  # UseBloodPressureCuff
    else:
        print(3)  # ExamineAirway