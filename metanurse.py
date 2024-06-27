while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # If no breathing detect immediate action
    if events[7] > 0:
        print(29)  # UseBagValveMask
        continue

    # Immediate attention to stabilize breathing
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Use Non-Rebreather Mask if Oxygen saturation is below 88% and above critical low level
    if measured_times[5] > 0 and 65 <= measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check vital signs if no recent valid measurement
    if any(time == 0 for time in measured_times[:3]):
        print(16)  # ViewMonitor
        continue

    # Update and stabilize as per vital measurements
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Stabilization check
    if (
        measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    # Default action if no immediate threats or actions applicable
    print(0)  # DoNothing