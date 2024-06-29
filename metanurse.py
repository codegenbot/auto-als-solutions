airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False
step_count = 0

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Terminate on 350 steps as a technical failure
    if step_count >= 350:
        print(48)  # Finish
        break

    step_count += 1

    # Immediately handle critical life-threatening conditions or interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0.7:  # AirwayClear detected
            airway_confirmed = True
        continue

    if not breathing_assessed and airway_confirmed:
        print(4)  # ExamineBreathing
        if events[10] > 0.7:  # BreathingEqualChestExpansion detected
            breathing_assessed = True
        continue

    if not circulation_checked and breathing_assessed:
        print(5)  # ExamineCirculation
        if events[16] > 0.7:  # RadialPulsePalpable detected
            circulation_checked = True
        continue

    if not disability_checked and circulation_checked:
        print(6)  # ExamineDisability
        if events[22] > 0.7 or events[25] > 0.7:  # AVPU_V or PupilsNormal detected
            disability_checked = True
        continue

    # Handling measurements
    if measured_times[4] <= 0:  # Blood pressure not measured recently
        print(27)  # UseBloodPressureCuff
        continue
    if measured_times[5] <= 0:  # Sats not measured recently
        print(25)  # UseSatsProbe
        continue

    # Stabilization achieved check
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