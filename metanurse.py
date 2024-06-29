airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_assessed = False
emergency_intervention_performed = False
steps = 0

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if events[7] >= 0.7 or (
        measured_times[6] > 0 and measured_values[6] < 8
    ):  # Severe Breathing Issues
        print(29)  # UseBagValveMask
        continue
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        airway_confirmed = True
        continue

    if airway_confirmed and not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    if airway_confirmed and breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    if circulation_checked and not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    if disability_checked and not exposure_assessed:
        print(7)  # ExamineExposure
        exposure_assessed = True
        continue

    if exposure_assessed and not emergency_intervention_performed:
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
        else:
            print(16)  # GiveFluids
            emergency_intervention_performed = True
            continue

    steps += 1
    if steps >= 350:
        print(48)  # Finish
        break