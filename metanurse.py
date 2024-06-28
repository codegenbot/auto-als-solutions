while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical condition checks
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check airway issues
    if events[3] < 0.5 and all(events[i] < 0.5 for i in [4, 5, 6]):  # Airway not clear
        print(3)  # ExamineAirway
        continue

    # Check breathing issues
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Oxygen saturation and respiratory rate
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation issues
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check overall stability
    conditions_met = (
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60
    )
    if conditions_met:
        print(48)  # Finish
        break

    # Routine action to collect more info
    print(16)  # ViewMonitor
  