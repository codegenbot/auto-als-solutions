while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediately critical conditions for cardiac arrest
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Ensure airway is checked early and adequately
    if events[3] == 0:  # if AirwayClear has never been checked (value is zero)
        print(3)  # ExamineAirway
        continue

    # Assisted breathing requirement checks
    if events[7] > 0.5:  # BreathingNone is high
        print(29)  # UseBagValveMask
        continue

    # Oxygen saturation targeting
    if measured_times[5] > 0:
        if measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue

    # Respiration rate handling
    if measured_times[6] > 0:
        if measured_values[6] < 8:
            print(29)  # UseBagValgetMask
            continue

    # Circulation support for low mean arterial pressure
    if measured_times[4] > 0:
        if measured_values[4] < 60:
            print(15)  # GiveFluids
            continue

    # Check if all stabilization criteria are met
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

    # Default action to further collect vital patient data
    if measured_times[4] == 0 and measured_times[5] == 0 and measured_times[6] == 0:
        print(27)  # UseBloodPressureCuff
        continue
    else:
        print(16)  # ViewMonitor