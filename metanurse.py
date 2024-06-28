while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical Conditions - Immediate chest compression
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check for Oxygen Saturation and MAP levels
    if measured_times[5] > 0:
        if measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask to increase O2 saturation
            continue

    if measured_times[4] > 0:
        if measured_values[4] < 60:
            print(15)  # GiveFluids for low MAP
            continue

    # Check if airway is obstructed
    if events[3] + events[4] + events[5] < 0.5:  # No recent clear airway event
        print(3)  # ExamineAirway
        continue

    # Check breathing status or initiate assistive measures
    if events[7] > 0.5 or (
        measured_times[6] > 0 and measured_values[6] < 8
    ):  # No breath or low breath rate
        print(29)  # UseBagValveMask
        continue

    # Once all conditions are stable, conclude the intervention
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

    # Default action if other specific actions are not necessary
    print(16)  # ViewMonitor or a default safe action like checking circulation again