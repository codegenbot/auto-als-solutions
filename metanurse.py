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

    # Immediate intervention for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Specific intervention based on observation advice
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Assess Airway initially, clear if necessary
    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0.5:  # AirwayClear is True
            airway_confirmed = True
        continue

    # Assess Breathing, verify conditions
    if airway_confirmed and not breathing_assessed:
        print(4)  # ExamineBreathing
        if events[10] > 0.5:  # Equal Chest Expansion is True
            breathing_assessed = True
        continue

    # Check Circulation, verify pulse and heart rate
    if breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
        if events[16] > 0.5:  # RadialPulsePalpable is True
            circulation_checked = True
        continue

    # Examine Disability, check consciousness levels
    if circulation_checked and not disability_checked:
        print(6)  # ExamineDisability
        if events[24] > 0.5 or events[23] > 0.5:  # PupilsNormal or PupilsPinpoint
            disability_checked = True
        continue

    # Ensure all assessments are done and vital signs are good
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
        if (
            measured_times[4] > 0
            and measured_values[4] >= 60
            and measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
        ):
            print(48)  # Finish
            break

    # Other necessary interventions and monitoring
    if measured_times[5] <= 0:
        print(25)  # UseSatsProbe
        continue

    if measured_times[4] <= 0:
        print(27)  # UseBloodPressureCuff
        continue

    print(16)  # ViewMonitor