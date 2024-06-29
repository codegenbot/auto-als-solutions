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

    # Check for immediate life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Sequential ABCDE examinations
    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1:  # Airway is clear
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue
        elif not breathing_assessed:
            if events[9] > 0:  # Breathing check related event detected
                breathing_assessed = True
            else:
                print(4)  # ExamineBreathing
                continue
        elif not circulation_checked:
            if (
                events[16] > 0 or events[17] > 0
            ):  # Circulation check (pulse palpable/non-palpable)
                circulation_checked = True
            else:
                print(5)  # ExamineCirculation
                continue
        elif not disability_checked:
            if events[22] > 0:  # Disability assessment (AVPU)
                disability_checked = True
            else:
                print(6)  # ExamineDisability
                continue
        elif not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue
        initial_assessments_done = True  # All initial assessments complete

    # Check stabilization conditions
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

    # Additional checks or repeated probes as required
    if not satsProbeUsed or measured_times[5] == 0 or measured_values[5] < 88:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        satsProbeRouteTaken = True
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(14)  # UseVenflonIVCatheter
        continue