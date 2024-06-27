while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    relevant_measures = list(map(float, inputs[39:46]))
    measures = list(map(float, inputs[46:]))

    if relevant_measures[5] > 0 and measures[5] < 65:
        print(17)  # StartChestCompression
        continue

    if relevant_measures[4] > 0 and measures[4] < 20:
        print(17)  # StartChestCompression
        continue

    if events[6] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    if events[3] > 0:  # AirwayClear
        if events[7] > 0:  # BreathingNone
            print(29)  # UseBagValveMask
        elif events[8] > 0 or events[9] > 0:  # BreathingSnoring or BreathingSeeSaw
            print(36)  # PerformHeadTiltChinLift
        else:
            print(4)  # ExamineBreathing
        continue
    elif (
        events[4] > 0 or events[5] > 0 or events[6] > 0
    ):  # AirwayVomit, AirwayBlood, AirwayTongue
        print(31)  # UseYankeurSuctionCatheter
        continue
    else:
        print(3)  # ExamineAirway
        continue

    if relevant_measures[4] > 0:
        if measures[4] < 60:  # MeasuredMAP
            print(15)  # GiveFluids
            continue
        else:
            print(5)  # ExamineCirculation
            continue
    else:
        print(27)  # UseBloodPressureCuff
        continue

    if events[22] > 0 or events[23] > 0 or events[24] > 0:  # AVPU_V or AVPU_P or AVPU_A
        print(6)  # ExamineDisability
        continue
    else:
        print(8)  # ExamineResponse
        continue

    if relevant_measures[5] > 0:
        if measures[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        else:
            print(25)  # UseSatsProbe
            continue
    else:
        print(4)  # ExamineBreathing
        continue

    if relevant_measures[6] > 0:
        if measures[6] < 8:
            print(29)  # UseBagValveMask
            continue
        else:
            print(25)  # UseSatsProbe
            continue

    if (
        (relevant_measures[5] > 0 and measures[5] >= 88)
        and (relevant_measures[6] > 0 and measures[6] >= 8)
        and (relevant_measures[4] > 0 and measures[4] >= 60)
    ):
        print(48)  # Finish
        break