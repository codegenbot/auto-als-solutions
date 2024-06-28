while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check immediate life threats
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Step 1: Check airway first
    if events[3] <= 0.5:
        if events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5:
            if events[5] > 0.5:  # AirwayBlood
                print(31)  # UseYankeurSucionCatheter
            else:
                print(32)  # UseGuedelAirway
        else:
            print(3)  # ExamineAirway
        continue

    # Step 2: Check breathing
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0:
        if measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue

    # Step 3: Check circulation
    if measured_times[4] > 0:
        if measured_values[4] < 60:  # MAP low
            print(15)  # GiveFluids
            continue

    # Step 4: Gather more information if critical conditions not met
    if measured_values[5] < 88 or measured_values[6] < 8 or measured_values[4] < 60:
        if events[0:3].count(0) == 3:  # No response events detected
            print(8)  # ExamineResponse
        elif events[24] < 0.5:  # No normal pupil response
            print(6)  # ExamineDisability
        else:
            print(16)  # ViewMonitor
        continue

    # Check if stabilisation criteria met
    stab_conditions_met = (
        events[3] > 0.5
        and measured_times[5] > 0  # AirwayClear
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    )
    if stab_conditions_met:
        print(48)  # Finish
        break

    # If no specific action taken, by default check circulation
    print(5)  # ExamineCirculation