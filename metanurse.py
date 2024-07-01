airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
monitorViewed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (
        not airway_confurred
        or not breathing_assessed
        or not circulation_checked
        or not disability_checked
        or not exposure_checked
    ):
        if not airway_confirmed and events[3] > 0:
            airway_confirmed = True
        elif not airway_confirmed:
            print(3)  # ExamineAirway
            continue

        if not breathing_assessed:
            if events[7] > 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
                print(29)  # UseBagValveMask
                continue
            else:
                print(4)  # ExamineBreathing
                breathing_assessed = True
                continue

        if not circulation_checked:
            if (measured_times[5] > 0 and measured_values[5] < 65) or (
                measured_times[4] > 0 and measured_values[4] < 20
            ):
                print(17)  # StartChestCompression
                continue
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

    else:
        initial_assessments_done = True

        if measured_times[5] == 0 or measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if measured_times[4] == 0 or measured_values[4] < 60:
            print(27)  # UseBloodPressureCuff
            continue

        if initial_assessments_done and (
            measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
            and measured_times[4] > 0
            and measured_values[4] >= 60
        ):
            print(48)  # Finish
            break

    print(0)  # DoNothing