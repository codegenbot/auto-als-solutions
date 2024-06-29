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

    if not airway_confirmed:
        if events[3] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
            airway_confirmed = True
            print(31)  # UseYankeurSucionCatheter
            continue
        else:
            print(3)  # ExamineAirway
            continue

    if not breathing_assessed:
        if measured_times[6] == 0 or measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue
        else:
            breathing_assessed = True

    if measured_times[5] == 0 or measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue

    if not circulation_checked:
        if measured_times[4] == 0 or measured_values[4] < 20:
            print(27)  # UseBloodPressureCuff
            continue
        else:
            circulation_checked = True

    if not disability_checked:
        if events[21] <= 0.1 and events[23] <= 0.1:
            print(6)  # ExamineDisability
            continue
        else:
            disability_checked = True

    if not emergency_intervention_performed:
        if (
            measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
            and measured_times[4] > 0
            and measured_values[4] >= 60
        ):
            emergency_intervention_performed = True
            print(48)  # Finish
            break
        else:
            print(16)  # ViewMonitor
            continue

    print(0)  # DoNothing if somehow reached here without conditions