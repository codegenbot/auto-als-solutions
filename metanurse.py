while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical condition checks for immediate life threats
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Examine important aspects in a structured manner -- ABCDE approach
    if events[3] < 0.5:  # Airway not clear indirectly
        print(3)  # ExamineAirway
        continue
    elif events[7] < 0.5:  # Significant breathing problem
        print(4)  # ExamineBreathing
        continue
    elif any(events[i] < 0.5 for i in range(16, 19)):  # Circulation doubts
        print(5)  # ExamineCirculation
        continue
    elif any(events[i] < 0.5 for i in range(21, 24)):  # Disability concerns
        print(6)  # ExamineDisability
        continue
    elif events[26] < 0.5:  # Exposure issues
        print(7)  # ExamineExposure
        continue

    # Oxygen saturation and respiratory rate checks against targets
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    elif measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation issues
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # General ability to measure vital signs
    if measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
        continue
    elif measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue
    elif measured_times[6] == 0:
        print(4)  # ExamineBreathing
        continue

    # Check overall stability and conditions for completion
    stable_conditions = (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    )
    if stable_conditions:
        print(48)  # Finish
        break

    # View monitor routinely to update info
    print(16)  # ViewMonitor