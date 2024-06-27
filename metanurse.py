while True:
    observations = input().split()
    relevance = list(map(float, observations[:39]))
    measurement_relevance = list(map(float, observations[39:46]))
    measurements = list(map(float, observations[46:]))

    # Check if any critical conditions are met
    if (measurement_relevance[5] > 0 and measurements[5] < 65) or (measurement_relevance[4] > 0 and measurements[4] < 20):
        print(17)  # StartChestCompression
        continue

    # Check airway
    if relevance[3] > 0:  # AirwayClear
        # Check breathing
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

    # Check circulation
    if measurement_relevance[4] > 0 and measurements[4] < 60:  # MeasuredMAP
        print(15)  # GiveFluids
    elif measurement_relevance[0] > 0 and measurements[0] < 60:  # MeasuredHeartRate
        print(10)  # GiveAdrenaline
    else:
        print(5)  # ExamineCirculation

    # Check disability
    if relevance[21] > 0 or relevance[22] > 0 or relevance[23] > 0:  # AVPU_U, AVPU_V, AVPU_P
        print(6)  # ExamineDisability
    else:
        print(8)  # ExamineResponse

    # Check exposure
    print(7)  # ExamineExposure

    # If oxygen saturation is below 88%
    if measurement_relevance[5] > 0 and measurements[5] < 88:
        print(30)  # UseNonRebreatherMask
    else:
        print(25)  # UseSatsProbe

    # If respiratory rate is below 8
    if measurement_relevance[6] > 0 and measurements[6] < 8:
        print(29)  # UseBagValveMask
    else:
        print(4)  # ExamineBreathing

    # Finish if stabilized
    if (measurement_relevance[5] > 0 and measurements[5] >= 88) and \
       (measurement_relevance[6] > 0 and measurements[6] >= 8) and \
       (measurement_relevance[4] > 0 and measurements[4] >= 60):
        print(48)  # Finish
        break