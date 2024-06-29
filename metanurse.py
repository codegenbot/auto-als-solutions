airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False

step_count = 0

while True:
    if step_count >= 350:
        print(48)  # Finish to avoid technical failure
        break

    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
            print(31)  # UseYankeurSuctionCatheter
            airway_confirmed = True
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        if events[8] > 0.1 or events[9] > 0.1 or events[10] > 0.1:
            print(29)  # UseBagValveMask
            breathing_assessed = True
        continue

    if not circulation_checked:
        print(5)  # ExamineCirculation
        if events[16] > 0.1 or measured_times[4] > 0 and measured_values[4] < 60:
            print(14)  # UseVenflonIVCatheter
            print(15)  # GiveFluids
            circulation_checked = True
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        if events[21] > 0.1 or events[23] > 0.1:
            disability_checked = True
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    if (measured_times[5] > 0 and measured_values[5] >= 88 and measured_times[6] > 0 and measured_values[6] >= 8 and measured_times[4] > 0 and measured_values[4] >= 60):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor
    step_count += 1