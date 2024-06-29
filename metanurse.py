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
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Check the airway
    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0.5:  # Check if Airway is clear
            airway_confirmed = True
        continue

    # If Airway is confirmed, check Breathing
    if airway_confirmed and not breathing_assessed:
        print(4)  # ExamineBreathing
        if events[10] > 0.5:  # Equal Chest Expansion
            breathing_assessed = True
        continue

    # If Breathing is assessed, check Circulation
    if breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
        if events[16] > 0.5:  # Radial Pulse Palpable
            circulation_checked = True
        continue

    # If Circulation is checked, check Disability
    if circulation_checked and not disability_checked:
        print(6)  # ExamineDisability
        if events[24] > 0.5 or events[23] > 0.5:  # Pupils Normal or Pinpoint
            disability_checked = True
        continue

    # If all assessments are done, ensure vital signs are good
    if airway_confirmed and breathing_assessed and circulation_checked and disability_checked:
        if (measured_times[4] > 0 and measured_values[4] >= 60) and \
           (measured_times[5] > 0 and measured_values[5] >= 88) and \
           (measured_times[6] > 0 and measured_values[6] >= 8):
            print(48)  # Finish
            break

    # Ensure Sats are checked if not done recently
    if measured_times[5] <= 0:
        print(25)  # UseSatsProbe
        continue

    # Ensure Blood Pressure is checked if not done recently
    if measured_times[4] <= 0:
        print(27)  # UseBloodPressureCuff
        continue

    # Monitor
    print(16)  # ViewMonitor