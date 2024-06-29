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

    # Critical conditions first
    if (measured_times[4] > 0 and measured_values[4] < 20) or (measured_times[5] > 0 and measured_values[5] < 65):
        print(17)  # StartChestCompression
        continue

    # Emergency breathing assistance
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Regular assessments loop
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue
    elif airway_confirmed and not breathing_assessed:
        print(4)  # ExamineBreathing
        continue
    elif breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
        continue
    elif circulation_checked and not disability_checked:
        print(6)  # ExamineDisability
        continue

    # Monitoring and direct actions based on hints
    if measured_times[5] == 0 or events[10] < 0.1:  # Low relevance or no oxygen sats taken yet
        print(25)  # UseSatsProbe
        continue
    elif measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
        continue

    # Evaluate vital signs and decide to do next
    if airway_confirmed and breathing_assessed and circulation_checked and disability_checked:
        if measured_times[5] > 0 and measured_values[5] >= 88:
            if measured_times[4] > 0 and measured_values[4] >= 60:
                if measured_times[6] > 0 and measured_values[6] >= 8:
                    print(48)  # Finish
                    break

    # If no specific actions are needed, monitor continuously
    print(16)  # ViewMonitor