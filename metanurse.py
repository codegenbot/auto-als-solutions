while True:
    observations = input().split()
    relevance = list(map(float, observations[:39]))
    measurement_relevance = list(map(float, observations[39:46]))
    measurements = list(map(float, observations[46:]))

    # Immediate life-threatening conditions
    if (measurement_relevance[5] > 0 and measurements[5] < 65) or (
        measurement_relevance[4] > 0 and measurements[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway Management
    if relevance[3] > 0:  # AirwayClear
        airway_ok = True
    elif (
        relevance[4] > 0 or relevance[5] > 0 or relevance[6] > 0
    ):  # AirwayVomit, AirwayBlood, AirwayTongue
        print(31)  # UseYankeurSuctionCatheter
        continue
    else:
        print(3)  # ExamineAirway
        continue

    # Breathing Assessment
    if relevance[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if relevance[8] > 0 or relevance[9] > 0:  # BreathingSnoring or BreathingSeeSaw
        print(36)  # PerformHeadTiltChinLift
        continue
    print(4)  # ExamineBreathing

    # Circulation Check
    if measurement_relevance[4] > 0 and measurements[4] < 60:  # MeasuredMAP
        print(15)  # GiveFluids
        continue
    if measurement_relevance[0] > 0 and measurements[0] < 60:  # MeasuredHeartRate
        print(10)  # GiveAdrenaline
        continue
    print(5)  # ExamineCirculation

    # Disability and Exposure
    print(6)  # ExamineDisability
    print(7)  # ExamineExposure

    # Measurements Monitoring
    if measurement_relevance[5] > 0:
        if measurements[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        else:
            print(25)  # UseSatsProbe
            continue

    # Check respiratory rate
    if measurement_relevance[6] > 0 and measurements[6] < 8:
        print(29)  # UseBagValveMask
        continue
    else:
        print(4)  # ExamineBreathing

    # Check if stabilized
    if (
        measurement_relevance[5] > 0
        and measurements[5] >= 88
        and measurement_relevance[6] > 0
        and measurements[6] >= 8
        and measurement_relevance[4] > 0
        and measurements[4] >= 60
    ):
        print(48)  # Finish
        break