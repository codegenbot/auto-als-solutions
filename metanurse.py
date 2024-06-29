airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False
steps_taken = 0

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
        if events[3] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    if airway_confirmed and not breathing_assessed:
        if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
            print(29)  # UseBagValveMask
            continue
        if events[10] > 0.1:
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
            continue

    if breathing_assessed and not circulation_checked:
        if events[16] > 0.1 or events[17] > 0.1:
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    if circulation_checked and not disability_checked:
        if events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1:
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

    if disability_checked and not emergency_intervention_performed:
        if (
            measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
            and measured_times[4] > 0
            and measured_values[4] >= 60
        ):
            if steps_taken < 3:
                steps_taken += 1
                print(16)  # ViewMonitor to verify stability
                continue
            print(48)  # Finish
            break
        else:
            print(16)  # ViewMonitor
            continue
    else:
        print(0)  # DoNothing if somehow reached here without conditions

    # Limit steps to prevent technical failure
    if steps_taken >= 349:
        print(0)  # DoNothing or any other safe non-altering state
        break
    steps_taken += 1