airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
steps = 0
satsProbeOpened = False
satsProbeUsed = False
measuring_bp = False

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
        if not airway_confirmed:
            if events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue

        if not breathing_assessed:
            if (
                events[7] > 0.2
                or events[8] > 0.2
                or events[9] > 0.2
                or events[10] > 0.2
                or events[11] > 0.2
                or events[12] > 0.2
                or events[13] > 0.2
                or events[14] > 0.2
            ):
                breathing_assessed = True
            else:
                print(4)  # ExamineBreathing
                continue

        if not circulation_checked:
            if events[16] > 0.2 or events[17] > 0.2:
                circulation_checked = True
            else:
                print(5)  # ExamineCirculation
                continue

        if not disability_checked:
            if events[21] > 0.2 or events[22] > 0.2 or events[23] > 0.2:
                disability_checked = True
            else:
                print(6)  # ExamineDisability
                continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    if satsProbeUsed and measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue

    if measured_times[5] != 0 and measured_values[5] < 88:
        if not satsProbeUsed:
            if not satsProbeOpened:
                print(19)  # OpenBreathingDrawer
                satsProbeOpened = True
            else:
                print(25)  # UseSatsProbe
                satsProbeUsed = True
            continue
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        if not measuring_bp:
            print(27)  # UseBloodPressureCuff
            measuring_bp = True
        else:
            print(38)  # TakeBloodPressure
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