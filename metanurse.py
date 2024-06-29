step_count = 0

airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False

while step_count < 350:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical condition checks
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        step_count += 1
        continue

    # Immediate treatment needs
    if (measured_times[6] > 0 and measured_values[6] < 8) or events[7] >= 0.7:
        print(29)  # UseBagValveMask
        step_count += 1
        continue

    # ABCDE Assessments
    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0.7:  # AirwayClear detected
            airway_confirmed = True
        step_count += 1
        continue

    if not breathing_assessed and airway_confirmed:
        print(4)  # ExamineBreathing
        if events[10] > 0.7:  # BreathingEqualChestExpansion detected
            breathing_assessed = True
        step_count += 1
        continue

    if not circulation_checked and breathing_assessed:
        print(5)  # ExamineCirculation
        if events[16] > 0.7:  # RadialPulsePalpable detected
            circulation_checked = True
        step_count += 1
        continue

    if not disability_checked and circulation_checked:
        print(6)  # ExamineDisability
        if events[22] > 0.7 or events[24] > 0.7:  # AVPU_V or PupilsNormal detected
            disability_checked = True
        step_count += 1
        continue

    # Ensuring monitoring
    if measured_times[4] <= 0:  # MAP not measured or outdated
        print(27)  # UseBloodPressureCuff
        step_count += 1
        continue
    elif measured_times[5] <= 0:  # Sats not measured or outdated
        print(25)  # UseSatsProbe
        step_count += 1
        continue

    # Final check if all needed conditions are met
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
            print(16)  # ViewMonitor
            step_count += 1
            continue

    # If nothing matches, default to monitor view
    print(16)  # ViewMonitor
    step_count += 1

    # Technical failure limit reached, force end
    if step_count >= 350:
        print(48)  # Finish
        break