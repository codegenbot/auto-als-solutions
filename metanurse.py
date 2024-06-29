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

    # Immediate life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Handle bag valve mask for severe breathing issues
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMass
        continue

    # Airway Examination and Confirmation
    if not airway_confirmed:
        if events[3] >= 0.5:  # AirwayClear observed robustly
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing Examination and Assessment
    if airway_confirmed and not breathing_assessed:
        if events[10] >= 0.5:  # BreathingEqualChestExpansion observed robustly
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
            continue

    # Circulation Examination
    if breathing_assessed and not circulation_checked:
        if events[16] >= 0.5:  # RadialPulsePalpable observed robustly
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    # Disability Examination
    if circulation_checked and not disability_checked:
        if events[24] >= 0.5:  # PupilsNormal observed robustly
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

    # Update inputs for oxygen saturation and blood pressure if they haven't been measured
    if measured_times[5] <= 0.1:  # Sats not measured or out-of-date
        print(25)  # UseSatsProbe
        continue

    if measured_times[4] <= 0.1:  # MAP not measured or out-of-date
        print(27)  # UseBloodPressureCuff
        continue

    # Check if stabilization criteria is met
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
        if (
            (measured_times[4] > 0 and measured_values[4] >= 60)
            and (measured_times[5] > 0 and measured_values[5] >= 88)
            and (measured_times[6] > 0 and measured_values[6] >= 8)
        ):
            print(48)  # Finish
            break
        else:
            # ViewMonitor for reassessment as needed
            print(16)  # ViewMonitor