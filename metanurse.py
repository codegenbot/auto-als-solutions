airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False
steps = 0

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
        emergency_intervention_performed = True
        continue

    # Basic airway examination and clearance
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    # Check for clear airway confirmation from events
    if not airway_confirmed and events[3] > 0.5:  # AirwayClear has high relevance
        airway_confirmed = True

    # Handling emergency interventions
    if emergency_intervention_performed:
        print(23)  # ResumeCPR if needed
        emergency_intervention_performed = False
        continue

    # Breathing assessment and stabilization
    if not breathing_assessed and airway_confirmed:
        print(25)  # UseSatsProbe to make sure Sats are measured
        print(4)  # ExamineBreathing
        if events[10] > 0.5:  # BreathingEqualChestExpansion has high relevance
            breathing_assessed = True
        continue

    # Circulation check
    if not circulation_checked and breathing_assessed:
        print(5)  # ExamineCirculation
        continue

    # Check for palpable pulse from events
    if (
        not circulation_checked and events[16] > 0.5
    ):  # RadialPulsePalpable has high relevance
        circulation_checked = True

    # Check and assess disability
    if not disability_checked and circulation_checked:
        print(6)  # ExamineDisability
        if (
            events[23] > 0.5 or events[24] > 0.5
        ):  # PupilsPinpoint or PupilsNormal has high relevance
            disability_checked = True
        continue

    # Ensure current measurements are taken if not done already
    if measured_times[4] <= 0:  # Blood pressure not measured recently
        print(27)  # UseBloodPressureCuff
        continue
    if measured_times[5] <= 0:  # Sats not measured recently
        print(25)  # UseSatsProbe
        continue
    if measured_times[6] <= 0:  # Resps not evaluated recently
        print(32)  # UseGuedelAirway in case airway stability is a concern
        continue

    # Monitor vital signs and handle stabilization
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
        if (
            measured_values[4] >= 60
            and measured_values[5] >= 88
            and measured_values[6] >= 8
        ):
            print(48)  # Finish scenario if stabilized
            break

    if steps > 350:
        break  # Escape after 350 steps to avoid infinite loop

    steps += 1
    print(16)  # ViewMonitor for general observation in the meantime