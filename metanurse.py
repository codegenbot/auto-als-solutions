while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate danger checks
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check airway states
    if events[2] > 0:  # ResponseNone (unresponsive)
        print(3)  # ExamineAirway
        continue

    # Clear obstruction in the airway
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirayBlood
        print(31)  # UseYankeurSucionCatheter
        continue

    # Check breathing status
    if events[7] > 0:  # BreathingNone
        if measured_times[5] == 0 or (
            measured_times[5] > 0 and measured_values[5] < 88
        ):
            print(30)  # UseNonRebreatherMask
            continue
        print(29)  # UseBagValveMask
        continue

    # Monitor and act on circulation problems
    if (measured_times[4] > 0 and measured_values[4] < 60) or measured_times[4] == 0:
        print(15)  # GiveFluids
        continue

    # Monitoring cases - ensure needed observations are up to date
    if events[39] == 0 or events[40] == 0 or events[41] == 0 or events[42] == 0:
        print(16)  # ViewMonitor
        continue

    # Improve Oxygen Saturation if needed
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Final check before finishing
    if (
        measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    # If no other actions are applicable
    print(0)  # DoNothing