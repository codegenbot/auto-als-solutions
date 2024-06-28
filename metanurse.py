while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    if measured_times[5] > 0:
        if measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if measured_values[5] >= 88:
            stable_sats = True
    else:
        print(16)  # ViewMonitor
        continue

    if measured_times[6] > 0:
        if measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue
        if measured_values[6] >= 8:
            stable_resps = True
    else:
        print(16)  # ViewMonitor
        continue

    if measured_times[4] > 0:
        if measured_values[4] < 60:
            print(15)  # GiveFluids
            continue
        if measured_values[4] >= 60:
            stable_map = True
    else:
        print(16)  # ViewMonitor
        continue

    if events[3] > 0.5:  # AirwayClear sufficiently recent and clear
        stable_airway = True
    else:
        print(3)  # ExamineAirway
        continue

    # Situation when all conditions are stabilized:
    if stable_airway and stable_sats and stable_resps and stable_map:
        print(48)  # Finish
        break

    print(0)  # DoNothing