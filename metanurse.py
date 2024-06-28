while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Directly address cardiac arrest signs
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Address Airway issues more consistently
    if max(events[4:8]) > 0:  # Detect any serious airway blockage
        print(32)  # UseGuedelAirway
        continue

    # Check and address breathing insufficiency robustly
    if events[7] >= 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Examine and intervene on circulation critically and repeatedly if needed
    if measured_times[4] == 0 or (measured_times[4] > 0 and measured_values[4] < 60):
        print(15)  # GiveFluids
        continue

    # Examine oxygen saturation and intervene as essential
    if measured_times[5] == 0 or (measured_times[5] > 0 and measured_values[5] < 88):
        print(30)  # UseNonRebreatherMask
        continue

    # Proper condition to finish the game based on problem stabilization statement
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

    # Emergency fallback to view the monitor if no action taken
    print(16)  # ViewMonitor