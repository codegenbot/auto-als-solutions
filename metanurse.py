while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue
    
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(32)  # UseGuedelAirway
        continue

    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

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

    if (
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing if nothing else is required