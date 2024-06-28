while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check if critical conditions leading to cardiac arrest exist
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Assess the airway
    if events[2] > 0:  # ResponseNone means checking airway is needed
        print(3)  # ExamineAirway
        continue

    # If vomit or blood in the airway is detected, clear it
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSucionCatheter
        continue

    # Ensure breathing
    if (
        events[7] > 0 and measured_times[6] == 0
    ):  # BreathingNone and no recent resp rate measurement
        print(4)  # ExamineBreathing
        continue

    # Ensure circulation if there's an existing measurement showing issues
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Obtain missing measurements for heart rate, respiration, and MAP if not measured or improving the oxygen level
    if measured_times[4] == 0 or measured_times[5] == 0 or measured_times[6] == 0:
        print(16)  # ViewMonitor
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # If all the stabilization conditions are met, finish the game
    if all(
        [
            measured_times[5] > 0 and measured_values[5] >= 88,
            measured_times[6] > 0 and measured_values[6] >= 8,
            measured_times[4] > 0 and measured_values[4] >= 60,
        ]
    ):
        print(48)  # Finish
        break

    # Default action if no immediate critical actions are necessary
    print(0)  # DoNothing