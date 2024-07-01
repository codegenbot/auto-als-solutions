airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # ABCDE assessments not done yet
    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            airway_confirmed = True
            continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            if not satsProbeUsed:
                print(25)  # UseSatsProbe
                satsProbeUsed = True
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            if not bpCuffUsed:
                print(27)  # UseBloodPressureCuff
                bpCuffUsed = True
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure = h_checked = True
            continue

        initial_assessments_done = True

    # Check for stabilization
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

    # Breathing problem handling
    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation problem handling
    if not bpCuffUsed:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(38)  # TakeBloodPressure
        continue

    # Default action
    print(0)  # DoNothing as last resort