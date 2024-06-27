while True:
    observations = input().split()
    relevance = list(map(float, observations[:39]))
    measurement_relevance = list(map(float, observations[39:46]))
    measurements = list(map(float, observations[46:]))

    # Immediate critical checks
    if (measurement_relevance[5] > 0 and measurements[5] < 65) or (measurement_relevance[4] > 0 and measurements[4] < 20):
        print(17)  # StartChestCompression
        continue
    
    # If breathing is none
    if relevance[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Evaluate Airways
    if relevance[4] > 0 or relevance[5] > 0 or relevance[6] > 0:  # AirwayVomit, AirwayBlood, AirwayTongue
        print(31)  # UseYankeurSuctionCatheter
        continue
    elif relevance[3] == 0:
        print(3)  # ExamineAirway
        continue

    # Evaluate Breathing
    if relevance[8] > 0 or relevance[9] > 0:  # BreathingSnoring or BreathingSeeSaw
        print(36)  # PerformHeadTiltChinLift
        continue
    elif measurement_relevance[5] > 0 and measurements[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    elif measurement_relevance[6] > 0 and measurements[6] < 8:
        print(29)  # UseBagValveMask
        continue
    else:
        print(4)  # ExamineBreathing
        continue

    # Evaluate Circulation
    if measurement_relevance[4] > 0 and measurements[4] < 60:
        print(15)  # GiveFluids
        continue
    elif measurement_relevance[0] > 0 and measurements[0] < 60:
        print(10)  # GiveAdrenaline
        continue
    else:
        print(5)  # ExamineCirculation
        continue

    # Evaluate Disability
    if relevance[22] > 0 or relevance[23] > 0:
        print(6)  # ExamineDisability
        continue
    else:
        print(8)  # ExamineResponse
        continue

    # Evaluate Exposure
    print(7)  # ExamineExposure
    continue

    # Stabilization Check
    if (measurement_relevance[5] > 0 and measurements[5] >= 88) and \
       (measurement_relevance[6] > 0 and measurements[6] >= 8) and \
       (measurement_relevance[4] > 0 and measurements[4] >= 60):
        print(48)  # Finish
        break

    # Fallback if no conditions met
    print(0)  # DoNothing