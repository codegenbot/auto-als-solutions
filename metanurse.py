airway_clear_confirmed = False
breathing_intervention_performed = False
circulation_intervention_performed = False
disability_checked = False
exposure_checked = False

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

    # Check airway
    if not airway_clear_confirmed:
        if events[3] > 0.5:  # AirwayClear
            airway_clear_confirmed = True
        print(3)  # ExamineAirway
        continue

    # Airway interventions if problems detected
    if any(
        events[i] > 0.5 for i in [1, 2, 4, 5, 6]
    ):  # Airway issues like Vomit, Blood, Tongue obstruction
        print(35)  # PerformAirwayManoeuvres
        continue

    # Check breathing
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

    # Check circulation
    if not circulation_intervention_performed:
        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
            continue

    # Check disability (consciousness)
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Check exposure
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Conditions for finishing
    if (
        airway_clear_confirmed
        and breathing_intervention_performed
        and circulation_intervention_performed
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