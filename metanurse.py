while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Flags
    airway_clear = breathing_checked = circulation_checked = disability_checked = False

    # Immediate checks for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Examine Airway
    if not airway_clear:
        if events[2] > 0 or events[3] > 0.5:  # AirwayClear or AirwayVomit
            airway_clear = True
        else:
            print(3)  # ExamineAirway
            continue

    # Check Breathing if Airway is clear
    if airway_clear and not breathing_checked:
        if events[7] > 0.5:  # No breathing detected
            print(29)  # UseBagValveMask
            continue
        if measured_times[6] > 0 and measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue
        if measured_times[5] > 0 and measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        breathing_checked = True

    # Check Circulation
    if breathing_checked and not circulation_checked:
        if measured_times[0] > 0 and measured_values[0] < 60 or measured_times[0] == 0:
            print(5)  # ExamineCirculation
            continue
        circulation_checked = True

    # Check Disability if Circulation is okay
    if circulation_checked and not disability_checked:
        if events[21] == 0:  # Unresponsive
            print(6)  # ExamineDisability
            continue
        disability_checked = True

    # Stability check before finishing
    if airway_clear and breathing_checked and circulation_checked and disability_checked:
        if events[3] > 0 and measured_values[5] >= 88 and measured_values[6] >= 8 and measured_values[4] >= 60:
            print(48)  # Finish
            break

    # Default safe observation
    print(16)  # ViewMonitor or any repeating required exam