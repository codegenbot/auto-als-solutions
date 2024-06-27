while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check immediate life-threatening conditions and act fast
    if (
        measured_times[5] > 0
        and measured_values[5] < 65
        or measured_times[4] > 0
        and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Examine ABCDE systematically, reacting to observations that are updated
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    # Optimization of monitor checking - only if required
    if any(mt == 0 for mt in measured_times):
        print(16)  # ViewMonitor
        continue

    # Check conditions for stabilization
    thresholds = [88, 8, 60]  # respective minimums for Sats, Resps, MAP
    stabilized = (
        measured_times[5] > 0
        and measured_values[5] >= thresholds[0]
        and measured_times[6] > 0
        and measured_values[6] >= thresholds[1]
        and measured_times[4] > 0
        and measured_values[4] >= thresholds[2]
    )

    if stabilized:
        print(48)  # Finish
        break

    print(0)  # DoNothing if nothing else is needed