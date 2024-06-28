while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate response for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Prioritize checking the airway
    if events[3] + events[4] + events[5] < 0.5:
        print(3)  # ExamineAirway
        continue

    # Check breathing sufficiency
    if events[7] > 0.5 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Manage insufficient oxygen saturation
    if measured_times[5] > 0:
        if measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue

    # Manage low mean arterial pressure
    if measured_times[4] > 0:
        if measured_values[4] < 60:
            print(15)  # GiveFluids
            continue

    # Final stability confirmation before finishing
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

    # Default action if other specific actions are not needed
    print(16)  # ViewMonitor as a default safe action