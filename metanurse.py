while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate actions for severe critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway management
    if events[2] > 0.1:  # ResponseNone indicates a possible airway issue
        print(3)  # ExamineAirway
        continue
    elif events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:  # Obstruction
        if events[5] > 0.1:  # AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
            continue
        elif events[4] > 0.1:  # AirwayVomit
            print(31)  # UseYankeurSuctionCatheter
            continue
        elif events[6] > 0.1:  # AirwayTongue observed
            print(32)  # UseGuedelAirway
            continue

    # Breathing management
    if events[7] > 0.1:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation management
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Re-checks if initial interventions insufficient
    if (
        measured_times[5] == 0
        or measured_values[5] < 88
        or measured_times[6] == 0
        or measured_values[6] < 8
        or measured_times[4] == 0
        or measured_values[4] < 60
    ):
        # Use sequence of examining ABCDE
        print(3)  # ExamineAirway
        continue

    if events[3] < 0.1 and events[4] < 0.1 and events[5] < 0.1 and events[6] < 0.1:
        # If airway is clear, check breathing and circulation next
        print(4)  # ExamineBreathing
        continue

    if (
        measured_values[5] >= 88
        and measured_values[6] >= 8
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default safe action
    print(16)  # ViewMonitor