while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life threats
    if measured_times[5] > 0:
        if measured_values[5] < 65:
            print(17)  # StartChestCompression if severe
            continue
        elif measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue

    # Check for Mean Arterial Pressure
    if measured_times[4] > 0:
        if measured_values[4] < 20:
            print(17)  # StartChestCompression for critical MAP
            continue
        elif measured_values[4] < 60:
            print(15)  # GiveFluids for low MAP
            continue

    # Ensure airway is clear
    if events[3] + events[4] + events[5] < 0.5:  # no recent clear airway event
        print(3)  # ExamineAirway
        continue

    # Check breathing or chest compression required
    if events[7] > 0.5 or (
        measured_times[6] > 0 and measured_values[6] < 8
    ):  # No breath or low breath rate
        print(29)  # UseBagValveMask
        continue

    # If all conditions are stable
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

    # If no specific action required, reassess systematically
    print(16)  # ViewMonitor or a default safe action like checking circulation again