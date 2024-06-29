airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
updates_needed = True

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Examinations to confirm statuses
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue
    if (
        not breathing_assessed and events[10] > 0.7
    ):  # BreathingEqualChestExpansion detected as true
        breathing_assessed = True

    if not circulation_checked and measured_times[4] > 0 and measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff if MAP is not recently measured
        circulation_checked = True
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        if (
            events[22] > 0.7 or events[24] > 0.7
        ):  # AVPU_V or PupilsNormal detected as true
            disability_checked = True
        continue

    # Ensure latest measurements for vital signs
    if measured_times[4] <= 0 or measured_times[5] <= 0 or measured_times[6] <= 0:
        if measured_times[4] <= 0:
            print(27)  # UseBloodPressureCuff
        elif measured_times[5] <= 0:
            print(25)  # UseSatsProbe
        elif measured_times[6] <= 0:
            print(26)  # UseAline for more frequent blood pressure monitoring
        continue

    # Check if stabilization criteria are met
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
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
        else:
            if updates_needed:
                print(16)  # ViewMonitor for current vital stats
                updates_needed = False
            else:
                print(0)  # DoNothing if all criteria are not met but no updates