airway_clear_confirmed = False
breathing_intervention_performed = False
circulation_intervention_performed = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway assessment and interventions
    if not airway_clear_confirmed or events[3] == 0:
        print(3)  # ExamineAirway
        continue
    if any([events[i] > 0.5 for i in [1, 2, 4, 5, 6]]):  # Airway problems
        print(35)  # PerformAirwayManoeuvres
        continue

    # Breathing assessment
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        breathing_intervention_performed = True
        continue

    # If airway is clear and no immediate breathing intervention is required:
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    elif measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation assessment
    if events[17] > 0.5:  # RadialPulseNonPalpable has high relevance
        print(17)  # StartChestCompression
        circulation_intervention_performed = True
        continue
    if not circulation_intervention_performed:
        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
            continue

    # Disability assessment
    if all(events[i] < 0.5 for i in [21, 22, 23, 24]):  # No responsive events detected
        print(6)  # ExamineDisability
        continue

    # Exposure assessment
    if events[26] > 0.5 or not all(
        measured_times
    ):  # ExposurePeripherallyShutdown or missing measurements
        print(7)  # ExamineExposure
        continue

    # Stabilization check
    if (
        airway_clear_confirmed
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Fall-back action to view monitor when other conditions are not met
    print(16)  # ViewMonitor