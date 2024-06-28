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

    # Initial Examinations
    if any(mt == 0 for mt in measured_times[:3]):
        if measured_times[0] == 0:
            print(3)  # ExamineAirway
        elif measured_times[1] == 0:
            print(4)  # ExamineBreathing
        elif measured_times[2] == 0:
            print(5)  # ExamineCirculation
        continue

    # Airway Assessment Improvement
    if events[3] > 0.5 or events[4] > 0.5 or events[5] > 0.5:  # Airway not clear
        print(3)  # ExamineAirway
        continue

    # Breathing and Airway Management
    if events[7] > 0.5:  # BreathingNone is true
        print(29)  # UseBagValveMask
        continue

    # Oxygen Saturation Management
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation Management
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Regular Checks and Monitoring
    print(16)  # ViewMonitor

    # Stability Check Before Finishing
    if (
        events[3] > 0.5
        and measured_values[5] >= 88
        and measured_values[6] >= 8
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default Fallback If Above Actions Are Not Required
    print(0)  # DoNothing