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

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed and (
            events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0
        ):
            airway_confirmed = True
        elif not airway_confirmed:
            print(3)  # ExamineAirway
            continue

        if (
            not breathing_assessed
            and events[7] < 0.7
            and measured_times[6] > 0
            and measured_values[6] >= 8
        ):
            breathing_assessed = True
        elif not breathing_assessed:
            print(4)  # ExamineBreathing
            continue

        # Ensure using Saturation Probe to measure oxygen level
        if measured_times[5] == 0:
            if not breathingDrawerOpened:
                print(19)  # OpenBreathingDrawer
                breathingDrawerOpened = True
                continue
            elif not satsProbeUsed:
                print(25)  # UseSatsProbe
                satsProbeUsed = True
                continue

        if not circulation_checked and (events[16] > 0 or events[17] > 0):
            circulation_checked = True
        elif not circulation_checked:
            print(5)  # ExamineCirculation
            continue

        if not disability_checked and (
            events[21] > 0 or events[22] > 0 or events[23] > 0
        ):
            disability_checked = True
        elif not disability_checked:
            print(6)  # ExamineDisability
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Intervention based on measurements
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0 or (measured_times[4] > 0 and measured_values[4] < 60):
        print(27)  # UseBloodPressureCuff
        continue

    if measured_times[6] == 0 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

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

    print(0)  # DoNothing as last resort