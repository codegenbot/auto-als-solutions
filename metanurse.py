airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False
step_counter = 0

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

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
        if events[7] == 0:
            print(4)  # ExamineBreathing
        else:
            breathing_assessed = True

    if breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    if circulation_checked and not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
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

    step_counter += 1
    if step_counter >= 350:
        print(48)  # Assume protocol asks to finish
        break

    print(16)  # ViewMonitor if somehow reached here without conditions