while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical condition checks for cardiac arrest scenario
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway check
    if events[3] < 0.5:  # AirwayClear is low, suspect airway problem
        print(3)  # ExεamineAirway
        continue

    # Primary response to no breathing detected
    if events[7] > 0.5:  # BreathingNone is high, urgent
        print(29)  # UseBagValveMask
        continue

    # Saturation and respiratory rate handling
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation issue - low mean arterial pressure
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check if conditions for stabilization are met
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

    # Default action to gather more information about the patient's state
    print(16)  # ViewMonitor