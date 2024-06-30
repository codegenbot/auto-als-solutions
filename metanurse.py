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

    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] >= 0.7:  # AirwayClear event identification
                airway_confirmed = True
                continue
            else:
                print(3)  # ExamineAirway to trigger/check condition
                continue

        elif not breathing_assessed:
            breathing_assessed = True
            print(4)  # ExamineBreathing
            continue

        elif not satsProbeUsed:
            satsProbeUsed = True
            print(25)  # UseSatsProbe
            continue

        elif not circulation_checked:
            circulation_checked = True
            print(5)  # ExamineCirculation
            continue

        elif not disability_checked:
            disability_checked = True
            print(6)  # ExamineDisability
            continue

        elif not exposure_checked:
            exposure_checked = True
            print(7)  # ExamineExposure
            continue

        initial_assessments_done = True

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

    elif measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    else:
        print(0)  # DoNothing if nothing else to do
        continue