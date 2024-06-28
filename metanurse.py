while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Emergency Checks for cardiac arrest
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check if the basic assessments have been done or updates are necessary
    if events[3] == 0:  # AirwayClear never checked
        print(3)  # ExamineAirway
    elif events[7] > 0.5:  # BreathingNone high presence
        print(29)  # UseBagValveMask
    elif measured_times[5] > 0 and measured_values[5] < 88:  # Low Sats
        print(30)  # UseNonRebreatherMask
    elif measured_times[6] > 0 and measured_values[6] < 8:  # Low respiration rate
        print(29)  # UseBagValveMask
    elif measured_times[4] > 0 and measured_values[4] < 60:  # Low MAP
        print(15)  # GiveFluids
    else:
        print(16)  # ViewMonitor

    # Check if conditions for patient stabilization are met
    if (
        (measured_times[5] > 0 and measured_values[5] >= 88)
        and (measured_times[6] > 0 and measured_values[6] >= 8)
        and (measured_times[4] > 0 and measured_values[4] >= 60)
    ):
        print(48)  # Finish
        break