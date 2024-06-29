airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False
initial_assessments_done = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate interventions for critical conditions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    # Initial ABCDE Assessments
    if not initial_assessments_done:
        if not airway_confirmed and events[3] > 0.1:
            airway_confirmed = True
        elif not airway_confirmed:
            print(3)  # ExamineAirway
            continue

        if not breathing_assessed and events[10] > 0.1:
            breathing_assessed = True
        elif not breathing_assessed:
            print(4)  # ExamineBreathing
            continue

        if not circulation_checked and (events[16] > 0.1 or events[17] > 0.1):
            circulation_checked = True
        elif not circulation_checked:
            print(5)  # ExamineCirculation
            continue

        if not disability_checked and (events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1):
            disability_checked = True
        elif not disability_checked:
            print(6)  # ExamineDisability
            continue
        
        initial_assessments_done = True
        print(7)  # ExamineExposure
        continue

    # Stabilization Actions
    if (
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break
    else:
        if measured_times[5] == 0 or measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
        elif measured_times[4] == 0 or measured_values[4] < 60:
            print(14)  # UseVenflonIVCatheter
            print(15)  # GiveFluids
        else:
            print(16)  # ViewMonitor