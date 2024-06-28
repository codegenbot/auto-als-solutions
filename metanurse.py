while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical Condition Immediate Response
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway Assessment Improvement
    if (
        events[3] + events[4] + events[5] < 0.5
        or events[1] + events[2]  # No clear airway sign
        > 0.5  # Onset breathing difficulty or obstruction signals
    ):
        print(3)  # ExamineAirway
        continue

    # Breathing Assessment Improvement
    if events[7] > 0.5:
        print(29)  # UseBagValveMask
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation Examination Based on Changes
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Stability Check Before Finishing
    if (
        events[3] > 0.5
        and measured_values[5] >= 88
        and measured_values[6] >= 8
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Regular Checks and Monitoring
    if any(
        mt == 0 for mt in measured_times[:3]
    ):  # If any vital signs haven't been measured recently
        print(16)  # ViewMonitor
        continue

    # Default Fallback If Above Actions Are Not Required
    print(0)  # DoNothing