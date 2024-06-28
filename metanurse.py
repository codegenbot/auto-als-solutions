while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate checks for life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check if airway is not clear
    if events[3] < 0.5 and (events[4] + events[5] + events[6] > 0.5):
        print(3)  # ExamineAirway
        continue

    # Check if breathing is insufficient or absent
    if events[7] > 0.5 or (measured_times[6] > 0 and measured_values[6] < 8):
        if events[13] > 0.5 or events[14] > 0.5:
            print(22)  # BagDuringCPR (Adjustment for severe breathing issues)
        else:
            print(29)  # UseBagValveMask
        continue

    # Check if oxygen saturation is below the safe threshold
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check Circulation - if mean arterial pressure is critically low
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check if conditions are met to stabilize patient
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

    # Default action to gather more information
    print(16)  # ViewMonitor