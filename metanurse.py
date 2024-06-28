while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if events[3] < 0.5 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue
    elif events[4] > 0 or events[5] > 0 or events[6] > 0:
        print(35)  # PerformAirwayManoeuvres
        continue

    if events[7] > 0.5:
        print(29)  # UseBagValveMask
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if events[22] > 0.5 or events[23] > 0.5:
        print(6)  # ExamineDisability
        continue

    if events[26] > 0.5:
        print(7)  # ExamineExposure
        continue

    if events[25] == 0 and events[26] == 0 and events[27] == 0:
        print(16)  # ViewMonitor
        continue

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