while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate checks for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check Airway
    if events[3] + events[4] + events[5] < 0.5:  # Airway not securely clear
        print(3)  # ExamineAirway
        continue

    # Check Breathing
    if events[7] > 0.5:  # No breathing detected
        print(29)  # UseBagValveMask
        continue

    # Check Circulation and respond accordingly
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Stability check before finishing
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

    # Default safe observation
    print(16)  # ViewMonitor generally or any repeating required exam