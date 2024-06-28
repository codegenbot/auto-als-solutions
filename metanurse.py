while True:
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

    # Check airway status
    if events[3] < 0.5:  # Low relevance for AirwayClear
        print(3)  # ExamineAirway
        continue

    # Check circulation pulse
    if events[17] > 0:  # RadialPulseNonPalpable significant
        print(5)  # ExamineCirculation
        continue

    # Breathing assessment and interventions
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation interventions
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Update Oxygen Saturation Monitoring
    if events[35] < 0.1 and measured_times[5] < 1:  # Check SatsProbe relevance
        print(25)  # UseSatsProbe
        continue

    # Stabilization check
    if (
        events[3] > 0.5  # AirwayClear
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and events[17] > 0.5  # RadialPulsePalpable
    ):
        # All conditions for stabilization met
        print(48)  # Finish
        break

    # Regular monitoring
    print(16)  # ViewMonitor