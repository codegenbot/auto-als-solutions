airway_clear = False
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

    if not airway_clear:
        if events[3] > 0.5:
            airway_clear = True
        else:
            print(3)  # ExamineAirway
            continue

    if events[7] > 0.5:
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if airway_clear:
        if measured_times[5] > 0 and measured_values[5] >= 88:
            if measured_times[6] > 0 and measured_values[6] >= 8:
                if measured_times[4] > 0 and measured_values[4] >= 60:
                    print(48)  # Finish
                    break

    print(16)  # ViewMonitor