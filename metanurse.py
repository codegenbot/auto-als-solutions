while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Assess response and airway immediately
    if events[2] > 0:  # ResponseNone
        print(3)  # ExamineAirway
        continue

    # Critical conditions first
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Airway checking
    if events[4] > 0:  # AirwayBlockage issue like AirwayVomit
        print(32)  # UseGuedelAirway
        continue

    # Breathing assistance
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Check circulation and breathing with a monitor
    if (
        measured_times[0] == 0 or measured_times[1] == 0
    ):  # Heart rate or resp rate not measured
        print(25)  # UseSatsProbe
        continue

    # Re-check necessary stats
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Circulation interventions
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Ensuring oxygenation
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Stabilization successful, finish the game
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

    # Default action if no immediate issues
    print(0)  # DoNothing