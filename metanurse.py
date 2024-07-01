airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
breathingDrawerOpened = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if not airway_confirmed:
        if events[3] > 0:
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    if not breathing_assessed:
        if events[10] > 0:  # BreathingEqualChestExpansion
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
            continue

    if not circulation_checked:
        if events[16] > 0:  # RadialPulsePalpable
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    if not disability_checked:
        if events[20] > 0:  # AVPU_A
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    initial_assessments_done = airway_confirmed and breathing_assessed and circulation_checked and disability_checked and exposure_checked

    if initial_assessments_done:
        if measured_times[5] < 0.1 or measured_values[5] < 88:
            if not satsProbeUsed:
                if not breathingDrawerOpened:
                    print(19)  # OpenBreathingDrawer
                    breathingDrawerOpened = True
                    continue
                print(25)  # UseSatsProbe
                satsProbeUsed = True
                continue
            print(30)  # UseNonRebreatherMask
            continue

        if measured_times[6] < 0.1 or measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue

        if measured_times[4] < 0.1 or measured_values[4] < 60:
            print(27)  # UseBloodPressureCuff
            continue

        if (measured_times[4] > 0 and measured_values[4] >= 60 and
            measured_times[5] > 0 and measured_values[5] >= 88 and
            measured_times[6] > 0 and measured_values[6] >= 8):
            print(48)  # Finish
            break

    print(0)  # DoNothing as last resort