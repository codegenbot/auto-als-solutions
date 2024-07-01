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

    if not satsProbeUsed and steps <= 3:
        if steps == 1:
            print(19)  # OpenBreathingDrawer
        elif steps == 2:
            print(25)  # UseSatsProbe
        else:
            print(16)  # ViewMonitor
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            if events[3] > 0:
                airway_confirmed = True
            continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            if events[7] > 0 or events[8] > 0:
                breathing_assessed = True
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            if events[16] > 0:
                circulation_checked = True
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            if events[21] > 0:
                disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
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

    print(0)  # DoNothing as last resort