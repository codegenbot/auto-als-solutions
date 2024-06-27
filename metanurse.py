while True:
    observations = input().split()
    relevance = list(map(float, observations[:39]))
    measurement_relevance = list(map(float, observations[39:46]))
    measurements = list(map(float, observations[46:]))

    if (measurement_relevance[5] > 0 and measurements[5] < 65) or (measurement_relevance[4] > 0 and measurements[4] < 20):
        print(17)  # StartChestCompression
        continue

    if relevance[6] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    if relevance[3] > 0:  # AirwayClear
        if relevance[7] > 0:  # BreathingNone
            print(29)  # UseBagValveMask
        elif relevance[8] > 0 or relevance[9] > 0:  # BreathingSnoring or BreathingSeeSaw
            print(36)  # PerformHeadTiltChinLift
        else:
            print(4)  # ExamineBreathing
    elif relevance[4] > 0 or relevance[5] > 0 or relevance[6] > 0:  # AirwayVomit, AirwayBlood, AirwayTongue
        print(31)  # UseYankeurSuctionCatheter
    else:
        print(3)  # ExamineAirway

    if measurement_relevance[4] > 0:
        if measurements[4] < 60:  # MeasuredMAP
            print(15)  # GiveFluids
        else:
            print(5)  # ExamineCirculation
    else:
        print(5)  # ExamineCirculation

    if relevance[22] > 0 or relevance[23] > 0:  # AVPU_V, AVPU_P
        print(6)  # ExamineDisability
    else:
        print(8)  # ExamineResponse

    print(7)  # ExamineExposure

    if measurement_relevance[5] > 0 and measurements[5] < 88:
        print(30)  # UseNonRebreatherMask
    elif measurement_relevance[5] == 0:
        print(25)  # UseSatsProbe

    if measurement_relevance[6] > 0 and measurements[6] < 8:
        print(29)  # UseBagValveMask
    elif measurement_relevance[6] == 0:
        print(4)  # ExamineBreathing

    if (measurement_relevance[5] > 0 and measurements[5] >= 88) and \
       (measurement_relevance[6] > 0 and measurements[6] >= 8) and \
       (measurement_relevance[4] > 0 and measurements[4] >= 60):
        print(48)  # Finish
        break