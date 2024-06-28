airway_clear_confirmed = False
breathing_intervention_performed = False
circulation_intervention_performed = False
disability_checked = False
exposure_checked = False
steps = 0

while steps < 350:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        breathing_intervention_performed = True
        continue

    if events[17] > 0.5:  # RadialPulseNonPalpable
        print(17)  # StartChestCompression
        circulation_intervention_performed = True
        continue

    # Airway Assessment
    if not airway_clear_confirmed:
        print(3)  # ExamineAirway
        if any(events[3:7] > 0.5 for i in range(4)):
            airway_clear_confirmed = True
        continue

    # Breathing Assessment
    if not breathing_intervention_performed:
        print(4)  # ExamineBreathing
        breathing_intervention_performed = True
        continue

    # Circulation Assessment
    if not circulation_intervention_performed:
        print(5)  # ExamineCirculation
        circulation_intervention_performed = True
        continue

    # Disability Assessment
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Exposure assessment
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Check if stabilised
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor
    steps += 1