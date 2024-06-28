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

    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        breathing_intervention_performed = True
        continue

    if events[17] > 0.5:  # RadialPulseNonPalpable
        print(17)  # StartChestCompression
        circulation_intervention_performed = True
        continue

    if not airway_clear_confirmed:
        if events[3] > 0.5:
            airway_clear_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Airway assessment and interventions
    if any([events[i] > 0.5 for i in [1, 2, 4, 5, 6]]):  # Airway problems
        print(35)  # PerformAirwayManoeuvres
        continue

    # Breathing assessment and interventions
    if not breathing_intervention_performed:
        if events[7] > 0.5:  # BreathingNone detected
            print(29)  # UseBagValveMask
            continue
        elif measured_times[5] > 0 and measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        elif measured_times[6] > 0 and measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue

    # Circulation interventions
    if not circulation_intervention_performed:
        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
            continue

    # Disability assessment
    if events[21] > 0.5 or events[22] > 0.5 or events[23] > 0.5 or events[24] > 0.5:
        # Already checked or detected response, do not recheck
        pass
    else:
        print(6)  # ExamineDisability
        continue

    # Exposure check
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
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

    print(16)  # ViewMonitor