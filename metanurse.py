while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions if in critical condition
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # The action plan may sequence through these exams only if the relevant measurements are outdated
    if not any(measured_times):  # None of the measurements are recent
        print(16)  # ViewMonitor to gather initial data
        continue

    # Actions based on the most detrimental and urgent issues
    if events[7] > 0.5:  # High relevance for BreathingNone
        if (
            events[8] > 0.5 or measured_values[5] < 88
        ):  # Snoring detected or low oxygen sats
            print(29)  # UseBagValveMask
        else:
            print(30)  # UseNonRebreatherMask
        continue

    # Check the airway status if unclear
    if (
        events[3] <= 0.5 and measured_times[5] > 0 and measured_values[5] < 88
    ):  # Airway not clearly examined and low sats
        print(3)  # ExamineAirway
        continue

    # Assessing breathing using advanced procedures
    if measured_times[5] > 0 and measured_values[5] < 88:  # Oxygen saturation critical
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:  # Respiratory rate too low
        print(29)  # UseBagValveMask
        continue

    # Monitoring and potentially improving circulation
    if measured_times[4] > 0 and measured_values[4] < 60:  # Low mean arterial pressure
        print(15)  # GiveFluids
        continue

    # Stabilization check
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish - patient is stabilized
        break

    # Check next relevant examination or monitoring view
    print(16)  # Regularly put back to ViewMonitor as a fallback action