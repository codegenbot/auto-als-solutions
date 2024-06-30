steps = 0
airway_checked = False
breathing_checked = False
circulation_checked = False
disability_checked = False
exposure_checked = False
sats_checked = False
while steps < 350:
    observations = input().split()
    # Extract observations into float lists
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Basic initial assessments
    if not airway_checked:
        print(3)  # ExamineAirway
        airway_checked = True
        continue

    if not breathing_checked:
        print(4)  # ExamineBreathing
        breathing_checked = True
        continue

    # Watching for quick application of oxygen or ventilation assistance
    if events[7] > 0.4:  # Respiration issues detected
        print(29)  # UseBagValveMask
        continue

    if not sats_checked and (measured_times[5] == 0 or measured_values[5] < 88):
        print(25)  # UseSatsProbe
        sats_checked = True
        continue

    if (
        measured_values[5] < 65 or measured_values[4] < 20
    ):  # Critical levels causing immediate risk
        print(17)  # StartChestCompression
        continue

    # Ensure all areas of ABCDE are checked
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Final check to end
    if (
        airway_checked
        and breathing_checked
        and circulation_checked
        and disability_checked
        and exposure_checked
    ):
        print(48)  # Finish
        break

    steps += 1