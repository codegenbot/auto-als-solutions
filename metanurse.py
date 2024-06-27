while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions checks
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Urgent conditions checks
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Recent airway blockages checks
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        if events[6] > 0:  # AirwayTongue
            print(32)  # UseGuedelAirway
        else:
            print(31)  # UseYankeurSuctionCatheter
        continue

    # Vital signs monitoring
    if measured_times[4] == 0 or measured_times[5] == 0 or measured_times[6] == 0:
        print(27)  # UseBloodPressureCuff
        continue

    # Examination blocks if needed information is missing
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue
    if sum(events[7:15]) == 0:
        print(4)  # ExamineBreathing
        continue
    if events[16] == 0 and events[17] == 0:
        print(5)  # ExamineCirculation
        continue
    if sum(events[21:24]) == 0:
        print(6)  # ExamineDisability
        continue
    if events[26] == 0 and events[27] == 0:
        print(7)  # ExamineExposure
        continue

    # Actions based on low vital signs
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Check for stabilized condition
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing if nothing else needs to be addressed