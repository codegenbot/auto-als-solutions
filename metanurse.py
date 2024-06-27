steps = 0

while steps < 350:
    observations = input().split()
    relevance = list(map(float, observations[:39]))
    measurement_relevance = list(map(float, observations[39:46]))
    measurements = list(map(float, observations[46:]))

    # Immediately handle life-threatening conditions
    if (measurement_relevance[5] > 0 and measurements[5] < 65) or (
        measurement_relevance[4] > 0 and measurements[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway Management
    if (
        relevance[4] > 0 or relevance[5] > 0 or relevance[6] > 0
    ):  # AirwayVomit, AirwayBlood, AirwayTongue
        print(31)  # UseYankeurSuctionCatheter
    elif relevance[3] > 0:  # AirwayClear
        print(36)  # PerformHeadTiltChinLift
    else:
        print(3)  # ExamineAirway

    # Breathing Management
    if relevance[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
    else:
        if measurement_relevance[5] > 0 and measurements[5] < 88:
            print(30)  # UseNonRebreatherMask
        else:
            print(4)  # ExamineBreathing

    # Circulation Management
    if measurement_relevance[4] > 0:
        if measurements[4] < 60:  # MeasuredMAP
            print(15)  # GiveFluids
        else:
            print(5)  # ExamineCirculation
    else:
        print(5)  # ExamineCirculation

    # Disability Management
    if relevance[22] > 0 or relevance[23] > 0:  # AVPU_V, AVPU_P
        print(6)  # ExamineDisability
    else:
        print(8)  # ExamineResponse

    # Exposure Management
    print(7)  # ExamineExposure

    # Finish the scenario if all conditions are met
    if (
        (measurement_relevance[5] > 0 and measurements[5] >= 88)
        and (measurement_relevance[1] > 0 and measurements[1] >= 8)
        and (measurement_relevance[4] > 0 and measurements[4] >= 60)
    ):
        print(48)  # Finish
        break

    steps += 1