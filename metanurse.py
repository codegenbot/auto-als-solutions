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

    # Enhanced logic to avoid repetitive unnecessary checks
    airway_clear_status = events[3] > 0
    severe_airway_issue = events[4] > 0 or events[5] > 0 or events[6] > 0

    if not airway_clear_status and not severe_airway_issue:
        print(3)  # ExamineAirway
        continue

    if severe_airway_issue:
        print(35)  # PerformAirwayManoeuvres
        continue

    # Severe breathing issues
    if events[7] > 0.5:
        print(29)  # UseBagValveMask
        continue

    # Breathing oxygen support
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation checks - fluids if low MAP, and regular checks if not done
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Disability assessment, check consciousness and respond
    if events[22] > 0.5 or events[23] > 0.5:
        print(6)  # ExamineDisability
        continue

    # Exposure assessment
    if events[26] > 0.5 or events[27] > 0.5:
        print(7)  # ExamineExposure
        continue

    # Regular monitoring and reassessment
    need_vitals_check = all(x == 0 for x in measured_times)
    if need_vitals_check:
        print(16)  # ViewMonitor
        continue

    # Decision to finish if stabilized
    is_stabilized = (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    )
    if is_stabilized:
        print(48)  # Finish
        break