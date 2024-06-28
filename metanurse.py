while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # First, manage emergency life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    # Check for clear airway or any blockages
    if events[3] <= 0.5:  # AirwayClear not confirmed
        print(3)  # ExamineAirway
        continue

    # Check breathing
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    elif measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check circulation
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Advanced checks if primary ones are ok
    if all(events[i] <= 0.5 for i in [1, 2, 4, 5, 6]) and events[3] > 0.5:  # Airway is clear
        if measured_times[6] > 0 and measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue
        if measured_times[5] > 0 and measured_values[5] >= 88 and measured_values[6] >= 8 and measured_values[4] >= 60:
            print(48)  # Finish - patient stabilized
            break
        print(16)  # ViewMonitor
        continue

    # If reached here, keep monitoring
    print(16)  # ViewMonitor