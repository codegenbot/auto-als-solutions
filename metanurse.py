while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Examine Airway and check if intervention is needed
    if events[3] < 0.05 or events[5] > 0.5 or events[6] > 0.5:  # Airway blockage indicators
        print(3)  # ExamineAirway
        continue

    # Check and manage breathing
    if measured_times[5] > 0 and measured_values[5] < 88:  # Low Oxygen saturation
        print(30)  # UseNonRebreatherMask
        continue

    if events[7] > 0.5:  # No breathing observed
        print(29)  # UseBagValveMask
        continue

    # Check and manage circulation
    if measured_times[4] > 0 and measured_values[4] < 60:  # Low MAP
        print(15)  # GiveFluids
        continue

    # Disability and Exposure Checks
    if events[21] > 0.5:  # AVPU Unresponsive
        print(32)  # UseGuedelAirway
        continue

    # Check for stabilization
    if (measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[1] > 0 and measured_values[1] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60):
        print(48)  # Finish
        break

    # Regular monitoring if no immediate action required
    print(16)  # ViewMonitor
