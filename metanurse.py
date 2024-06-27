while True:
    observations = input().split()
    relevance = list(map(float, observations[:39]))
    measurement_relevance = list(map(float, observations[39:46]))
    measurements = list(float, observations[46:])

    # Immediate critical conditions for cardiac arrest
    if (measurement_relevance[5] > 0 and measurements[5] < 65) or (measurement_relevance[4] > 0 and measurements[4] < 20):
        print(17)  # StartChestCompression
        continue

    # Manage airway
    if relevance[3] > 0:  # AirwayClear
        airway_clear = True
    elif relevance[4] > 0 or relevance[5] > 0 or relevance[6] > 0:  # Airway obstructed by vomit, blood, or tongue
        print(31)  # UseYankeurSuctionCatheter
        continue
    else:
        print(3)  # ExamineAirway
        continue

    # Manage breathing
    if relevance[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
    elif relevance[8] > 0 or relevance[9] > 0:  # BreathingSnoring or BreathingSeeSaw
        print(36)  # PerformHeadTiltChinLift
    else:
        print(4)  # ExamineBreathing

    # Circulation checks
    if relevance[16] > 0:  # RadialPulsePalpable
        pulse_ok = True
    elif relevance[17] > 0:  # RadialPulseNonPalpable
        print(10)  # GiveAdrenaline
        continue
    if measurement_relevance[0] > 0 and measurements[0] < 60:  # MeasuredHeartRate low
        print(10)  # GiveAdrenaline
        continue
    if measurement_relevance[4] > 0 and measurements[4] < 60:  # MeasuredMAP low
        print(15)  # GiveFluids
        continue
    else:
        print(5)  # ExamineCirculation

    # Disability assessment
    if relevance[21] > 0 or relevance[22] > 0 or relevance[23] > 0:  # AVPU_U, AVPU_V, AVPU_P
        print(6)  # ExamineDisability
    else:
        print(8)  # ExamineResponse

    # Exposure check
    print(7)  # ExamineExposure

    # Oxygen and breathing support
    if measurement_relevance[5] > 0:
        if measurements[5] < 88:
            print(30)  # UseNonRebreatherMask
        else:
            print(25)  # UseSatsProbe

    # Finish if stabilized
    if (measurement_relevance[5] > 0 and measurements[5] >= 88) and \
       (measurement_relevance[6] > 0 and measurements[6] >= 8) and \
       (measurement_relevance[4] > 0 and measurements[4] >= 60):
        print(48)  # Finish
        break