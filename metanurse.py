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

    # Assessments should confirm all data is collected first
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue
    elif not breathing_assessed:
        print(4)  # ExamineBreathing
        continue
    elif not circulation_checked:
        print(5)  # ExamineCirculation
        continue
    elif not disability_checked:
        print(6)  # ExamineDisability
        continue
    elif not emergency_intervention_performed:
        print(7)  # ExamineExposure
        emergency_intervention_performed = True
        continue

    # Begin treatment based on assessments
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(14)  # UseVenflonIVCatheter
        print(15)  # GiveFluids
        continue

    if measured_times[5] > 0 and measured_values[5] >= 88 and measured_times[6] > 0 and measured_values[6] >= 8 and measured_times[4] > 0 and measured_values[4] >= 60:
        print(48)  # Finish
        break

    print(16)  # ViewMonitor to reassess and make next decisions based on updated vitals