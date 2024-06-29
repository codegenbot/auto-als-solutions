airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False

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

    if events[6] > 0:
        airway_confirmed = True

    if airway_confirmed and not breathing_assessed:
        if events[13] > 0:
            breathing_assessed = True

    if breathing_assessed and not circulation_checked:
        if events[16] > 0 or events[17] > 0:
            circulation_checked = True

    if circulation_checked and not disability_checked:
        if events[21] > 0 or events[22] > 0:
            disability_checked = True

    if not airway_confirmed:
        print(3)  # ExamineAirway
    elif not breathing_assessed:
        print(4)  # ExamineBreathing
    elif not circulation_checked:
        print(5)  # ExamineCirculation
    elif not disability_checked:
        print(6)  # ExamineDisability
    else:
        if measured_times[4] <= 0:  # Blood pressure not measured recently
            print(27)  # UseBloodPressureCuff
        elif measured_times[5] <= 0:  # Sats not measured recently
            print(25)  # UseSatsProbe
        else:
            if (
                measured_values[5] >= 88
                and measured_values[6] >= 8
                and measured_values[4] >= 60
            ):
                print(48)  # Finish
                break
            else:
                print(16)  # ViewMonitor