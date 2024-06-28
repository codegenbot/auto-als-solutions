while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Start Chest Compressions immediately in critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check the Airway
    if events[3] <= 0.5:  # No recent clear airway event
        if events[4] + events[5] + events[6] > 0.1:  # Obstruction indications
            print(3)  # ExamineAirway
            continue
        if (
            events[7] + events[8] > 0.1
        ):  # Breathing issues might indicate airway problem
            print(3)  # ExamineAirway
            continue

    # Breathing interventions
    if events[7] > 0.5:  # No breathing detected
        print(29)  # UseBagValveMask
        continue

    # Check oxygen saturation and respirations
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # useBagValveMask
        continue

    # Circulation Checks
    if measured_times[0] > 0 and (
        events[16] < 0.5 or events[17] > 0.5
    ):  # Pulse problems
        print(5)  # ExamineCirculation
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Stabilization check
    if (
        events[3] > 0.5
        and measured_values[5] >= 88
        and measured_values[6] >= 8
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # If patient is generally stable, monitor with equipment
    print(16)  # ViewMonitor