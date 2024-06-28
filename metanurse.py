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
    if events[3] < 0.5 and all(events[i] < 0.5 for i in range(4, 7)):
        print(3)  # ExamineAirway
        continue
    if any(
        events[i] > 0.5 for i in [4, 5, 6]
    ):  # Airway blockage due to vomit, blood or tongue
        print(31)  # UseYankeurSuctionCatheter
        continue

    # Breathing problems
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Oxygen saturation and respiratory rate
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[1] > 0 and measured_values[1] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation status
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check other vitals and actions if above critical conditions are not met
    # Mostly restoration and collection of information if no immediate life threats detected
    flag_complete = (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[1] > 0
        and measured_values[1] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    )

    if flag_complete:
        print(48)  # Finish
        break

    # Routine actions for information collection
    print(16)  # ViewMonitor