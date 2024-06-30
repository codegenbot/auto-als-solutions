airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical condition checks
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            continue
        elif events[3] > 0:
            airway_confirmed = True

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            continue
        elif any(events[i] > 0 for i in [10, 11, 12, 13, 14]):
            breathing_assessed = True
            if not satsProbeUsed:
                print(25)  # UseSatsProbe
                satsProbeUsed = True

        if not circulation_checked:
            print(5)  # ExamineCirculation
            continue
        elif any(events[i] > 0 for i in [16, 17]):
            circulation_checked = True

        if not disability_checked:
            print(6)  # ExamineDisability
            continue
        elif any(events[i] > 0 for i in [21, 22, 23]):
            disability_checked = True

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Action based on measurements after initial assessments
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    # If all conditions are met for stabilization
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