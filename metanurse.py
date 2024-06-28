while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions
    if measured_times[5] > 0:
        if measured_values[5] < 65:  # Extremely low oxygen saturation
            print(17)  # StartChestCompression
            continue
        elif measured_values[5] < 88:  # Insufficient oxygen saturation
            print(30)  # UseNonRebreatherMask
            continue

    if measured_times[4] > 0:
        if measured_values[4] < 20:  # Extremely low MAP
            print(17)  # StartChestCompression
            continue
        elif measured_values[4] < 60:  # Insufficient MAP
            print(15)  # GiveFluids
            continue

    # Airway management based on events
    if events[6] > 0.5:  # Airway obstructed by tongue
        print(35)  # PerformAirwayManoeuvres
        continue
    else:
        print(3)  # ExamineAirway generally if not recently checked
        continue

    # Breathing management
    if events[7] > 0.5 or (
        measured_times[6] > 0 and measured_values[6] < 8
    ):  # No breathing or low respiratory rate
        print(29)  # UseBagValveBehold mask
        continue

    # Regular monitoring and checks
    if measured_times[6] == 0 or measured_times[5] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor to get latest readings
        continue

    # Check conditions to finish
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

    # Default action if no specific treatment is required
    print(0)  # DoNothing