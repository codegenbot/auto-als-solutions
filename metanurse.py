airway_clear_confirmed = False
breathing_intervention_needed = False
circulation_intervention_needed = False

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

    # Check airway
    if not airway_clear_confirmed:
        if events[3] > 0.5:  # AirwayClear
            airway_clear_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Handle Airway problems
    if any(events[i] > 0.5 for i in [4, 5, 6]):  # AirwayVomit, AirwayBlood, AirwayTongue
        print(35)  # PerformAirwayManoeuvres
        continue

    # Immediate breathing interventions
    if events[7] > 0.5 or (measured_times[6] > 0 and measured_values[6] < 8):  # BreathingNone or low resps
        print(29)  # UseBagValveMask
        breathing_intervention_needed = True
        continue

    # Check if breathing needs assistance
    if not breathing_intervention_needed and (measured_times[5] > 0 and measured_values[5] < 88):
        print(30)  # UseNonRebreatherMask
        continue

    # Urgent circulation checks
    if events[17] > 0.5:  # RadialPulseNonPalpable
        print(17)  # StartChestCompression
        circulation_intervention_needed = True
        continue

    # Handle circulation problems
    if not circulation_intervention_needed and (measured_times[4] > 0 and measured_values[4] < 60):
        print(15)  # GiveFluids
        continue

    # Check disability status
    if events[21] > 0.5 or events[22] > 0.5 or events[23] > 0.5 or events[24] > 0.5:
        pass  # Already checked or detected response
    else:
        print(6)  # ExamineDisability
        continue

    # Exposure
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue
    
    # Stabilization complete check
    if (airway_clear_confirmed and breathing_intervention_needed and circulation_intervention_needed and
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60):
        print(48)  # Finish
        break

    # Monitor patient
    print(16)  # ViewMonitor