while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions
    if measured_values[5] < 65 or measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Examine airway if not clear or high relevance of obstructions
    if events[3] < 0.5 and (events[4] + events[5] + events[6] > 0.5):
        print(3)  # ExamineAirway
        continue

    # Handle Breathing Issues
    measured_breathing = measured_times[6] > 0 and measured_values[6] >= 8
    if not measured_breathing:
        print(4)  # ExamineBreathing
        continue
    if measured_breathing:
        if events[11] > 0.5:  # BreathingBibasalCrepitations relevant
            print(29)  # UseBagValveMask if respiratory issues
            continue

    # Oxygen saturation below threshold and not in critical condition
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Low Mean Arterial Pressure but not yet critical
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Winning condition
    if measured_values[5] >= 88 and measured_values[6] >= 8 and measured_values[4] >= 60:
        print(48)  # Finish
        break

    # Measurement assessments not initiated or outdated
    if measured_times[6] == 0:  # Checking respiration rate
        print(4)  # ExamineBreathing
    elif measured_times[5] == 0:  # Oxygen saturation not measured
        print(25)  # UseSatsProbe
    elif measured_times[4] == 0:  # MAP not measured
        print(27)  # UseBloodPressureCuff
    else:
        print(5)  # ExamineCirculation