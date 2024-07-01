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

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            continue

        if events[3] > 0:  # AirwayClear
            airway_confirmed = True

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            if (
                events[7] > 0
                or events[8] > 0
                or events[9] > 0
                or events[10] > 0
                or events[11] > 0
            ):
                breathing_assessed = True
            continue

        if not satsProbeUsed:
            print(25)  # UseSatsProbe
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            continue

        if (
            events[16] > 0 or events[17] > 0 or measured_values[4] < 60
        ):  # MeasuredMAP is low
            circulation_checked = True

        if not disability_checked:
            print(6)  # ExamineDisability
            continue

        if events[21] > 0 or events[22] > 0:
            disability_checked = True

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if not bpCuffUsed:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(38)  # TakeBloodPressure
        continue

    if (
        measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
    ):
        if (measured_times[6] > 0 and measured_values[6] >= 8) or events[7] > 0.7:
            print(48)  # Finish
            break

    print(0)  # DoNothing as last resort