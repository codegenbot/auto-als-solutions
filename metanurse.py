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

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            airway_confirmed = events[3] > 0  # Assume we get feedback on airway status
            continue
        if not breathing_assessed:
            breathing_assessed = (
                events[7] > 0 or events[11] > 0
            )  # Check breathing status feedback logic
            print(4)  # ExamineBreathing
            continue
        if not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = (
                events[16] > 0 or events[17] > 0
            )  # Check circulation status feedback logic
            continue
        if not disability_checked:
            print(6)  # ExamineDisability
            # Additional logic needed based on observations for disability confirmation
            continue
        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue
        initial_assessments_done = True

    if initial_assessments_done:
        if airway_confirmed and breathing_assessed and circulation_checked:
            if (
                (measured_times[5] > 0 and measured_values[5] >= 88)
                and (measured_times[6] > 0 and measured_values[6] >= 8)
                and (measured_times[4] > 0 and measured_values[4] >= 60)
            ):
                print(48)  # Finish
                break

    if not satsProbeUsed:
        if measured_times[5] == 0 or measured_values[5] < 88:
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue