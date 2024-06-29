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

    # Handle immediate life-threatening conditions
    if (measured_times[6] > 0 and measured_values[6] < 8) or events[7] >= 0.7:
        print(29)  # UseBagValveMask
        continue
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Examination sequence
    if not airway_confirmed:
        if events[3] > 0.7:  # AirwayClear detected
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    if not breathing_assessed and airway_confirmed:
        if events[10] > 0.7:  # BreathingEqualChestExpansion detected
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
            continue

    if not circulation_checked and breathing_assessed:
        if events[16] > 0.7:  # RadialPulsePalpable detected
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    if not disability_checked and circulation_checked:
        if events[22] > 0.7 or events[24] > 0.7:  # AVPU_V or PupilsNormal detected
            disability_checked = true
        else:
            print(6)  # ExamineDisability
            continue

    # Ensure vital measurements are up-to-date
    if (
        measured_times[4] <= 0 or measured_values[4] < 60
    ):  # Blood pressure not adequate or not measured
        print(27)  # UseBloodPressureCuff
        continue
    if (
        measured_times[5] <= 0 or measured_values[5] < 88
    ):  # Sats not adequate or not measured
        print(25)  # UseSatsProbe
        continue
    if (
        measured_times[6] <= 0 or measured_values[6] < 8
    ):  # Respiratory rate not adequate or not measured
        print(16)  # ViewMonitor
        continue

    # Check if all assessments done and patient stable
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
        print(48)  # Finish
        break