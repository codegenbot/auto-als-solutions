steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))
    
    # Immediate critical actions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # ABCDE assessment progression
    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] >= 0.7:  # AirwayClear event identification
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway to trigger/check condition
            continue

        elif not breathing_assessed:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

        elif not satsProbeUsed:
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue
        
        elif not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        elif not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        elif not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Once stabilized, finish
    if initial_assessments_done and (
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    elif measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    else:
        print(0)  # DoNothing if nothing else to do
        continue