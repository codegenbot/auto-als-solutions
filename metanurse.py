while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions that require urgent actions
    if measured_times[5] > 0:
        if measured_values[5] < 65:
            print(17)  # StartChestCompression
            continue
        elif measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue

    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Airway management
    if events[3] < 0.5 and all(events[i] < 0.5 for i in range(4, 7)):
        print(3)  # ExamineAirway
        continue
    if events[3] < 0.1:
        print(36)  # PerformHeadTiltChinLift
        continue

    # Breathing checks and management
    if measured_times[1] > 0 and measured_values[1] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation check
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check and reassess as necessary
    if any(t == 0 for t in measured_times[1:6]):  # any vital signs not measured recently
        print(16)  # ViewMonitor
        continue

    # Stability check before finishing
    airway_clear = events[3] > 0.5
    breathing_stable = (measured_times[1] > 0 and measured_values[1] >= 8) and (measured_times[5] > 0 and measured_values[5] >= 88)
    circulation_stable = measured_times[4] > 0 and measured_values[4] >= 60

    if airway_clear and breathing_stable and circulation_stable:
        print(48)  # Finish
        break

    # Default passive action if no other actions are required
    print(0)  # DoNothing