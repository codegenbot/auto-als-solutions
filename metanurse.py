airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False
measurements_updated = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue
    if not breathing_assessed and airway_confirmed:
        print(4)  # ExamineBreathing
        continue
    if not circulation_checked:
        print(5)  # ExamineCirculation
        continue
    if not measurements_updated:
        if measured_times[4] <= 0:
            print(27)  # UseBloodPressureCuff
            continue
        if measured_times[5] <= 0:
            print(25)  # UseSatsProbe
            continue
        measurements_updated = True
    
    if emergency_intervention_performed:
        if measured_times[5] > 0 and measured_values[5] >= 88 and measured_times[6] > 0 and measured_values[6] >= 8 and measured_times[4] > 0 and measured_values[4] >= 60:
            print(48)  # Finish
            break
        else:
            print(16)  # ViewMonitor
            continue
    else:
        print(16)  # ViewMonitor