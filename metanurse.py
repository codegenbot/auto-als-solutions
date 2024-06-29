airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False

count = 0

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
        if events[3] > 0.7:
            airway_confirmed = True
        continue

    if not breathing_assessed and airway_confirmed:
        print(4)  # ExamineBreathing
        if events[10] > 0.7:
            breathing_assessed = True
        continue

    if not circulation_checked and breathing_assessed:
        print(5)  # ExamineCirculation
        if events[16] > 0.7:
            circulation_checked = True
        continue

    if not disability_checked and circulation_checked:
        print(6)  # ExamineDisability
        if events[23] > 0.7 or events[24] > 0.7:
            disability_checked = True
        continue

    if measured_times[5] <= 0:
        print(25)  # UseSatsProbe
        continue

    if measured_times[4] <= 0:
        print(27)  # UseBloodPressureCuff
        continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    count += 1
    if count >= 350:
        break

    print(16)  # ViewMonitor