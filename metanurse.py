while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    critical_sats = measured_times[5] > 0 and measured_values[5] < 65
    critical_map = measured_times[4] > 0 and measured_values[4] < 20

    # Immediate response for critical conditions
    if critical_sats or critical_map:
        print(17)  # StartChestCompression
        continue

    # Airway examination strategy
    airway_blocked = events[4] > 0 or events[5] > 0
    if airway_blocked or sum(events[3:6]) == 0:
        print(3)  # ExamineAirway
        continue

    # Breathing assessment
    insufficient_breathing = events[7] > 0 or (measured_times[6] > 0 and measured_values[6] < 8)
    if insufficient_breathing:
        print(29)  # UseBagValveMask
        continue

    # Oxygen saturation management
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation issues: monitor mean arterial pressure
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Checking stability before finishing the scenario
    stable_conditions = (
        events[3] > 0 and
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60
    )
    if stable_conditions:
        print(48)  # Finish
        break

    # Default safe action if other specific actions are not needed
    print(16)  # ViewMonitor