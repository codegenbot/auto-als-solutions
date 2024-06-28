while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway management
    if (
        events[2] < 0.5
        and events[3] < 0.5
        and all(events[i] < 0.5 for i in range(4, 7))
    ):
        print(3)  # ExamineAirway
        continue
    if any(
        events[i] > 0.5 for i in [4, 5, 6]
    ):  # Airway blockage due to vomit, blood or tongue
        print(31)  # UseYankeurSuctionCatheter
        continue

    # If airway clear, check Breathing and Circulation
    if events[3] > 0.5:
        print(4)  # ExamineBreathing
        continue
    if measured_values[4] > 60:  # Measured MAP safe
        print(25)  # UseSatsProbe
        continue

    # Handle potential circulatory problems
    if measured_values[1] < 8:  # Resp rate low
        print(29)  # UseBagValimmerMask
        continue
    if measured_values[5] < 88:  # Saturation low
        print(30)  # UseNonRebreatherMask
        continue
    if measured_values[4] < 60:  # MAP low
        print(15)  # GiveFluids
        continue

    # Check Circulation status
    if (
        events[17] > 0.5
    ):  # RadialPulseNonPalpable indicates serious problem with circulation
        print(17)  # StartChestCompression
        continue

    # Check other vital stats
    if measured_times[4] == 0 or measured_values[4] < 60:  # MAP check
        print(27)  # UseBloodPressureCuff
        continue

    # Regular monitoring
    print(16)  # ViewMonitor

    # Final check to determine if scenario is stabilized
    flag_complete = (
        events[3] > 0.5
        and measured_values[4] >= 60
        and measured_values[1] >= 8
        and measured_values[5] >= 88
    )
    if flag_complete:
        print(48)  # Finish
        break