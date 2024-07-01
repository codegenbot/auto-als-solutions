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

    # Start chest compressions if critical conditions are met
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0.1:
            airway_confirmed = True
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        if any(
            events[i] > 0.1 for i in range(8, 14)
        ):  # Check any relevant breathing event
            breathing_assessed = True
        continue

    if not satsProbeUsed:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        print(16)  # ViewMonitor
        satsProbeUsed = True
        continue

    if not circulation_checked:
        print(5)  # ExamineCirculation
        if (
            events[16] > 0.1 or events[17] > 0.1
        ):  # RadialPulsePalpable, RadialPulseNonPalpable
            circulation_checked = True
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        if events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1:  # AVPU conditions
            disability_checked = True
        continue

    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    initial_assessments_done = True

    if initial_assessments_done:
        correct_breathing = False
        correct_circulation = False

        if measured_times[5] > 0 and measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        elif measured_times[5] > 0 and measured_values[5] >= 88:
            correct_breathing = True

        if measured_times[4] > 0 and measured_values[4] < 60:
            print(27)  # UseBloodPressureCuff
            print(38)  # TakeBloodPressure
            continue
        elif measured_times[4] > 0 and measured_values[4] >= 60:
            correct_circulation = True

        if correct_breathing and correct_circulation:
            print(48)  # Finish
            break

    print(0)  # DoNothing