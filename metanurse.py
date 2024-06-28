while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical response
    if measured_times[5] > 0 and measured_values[5] < 65 or measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Airway management
    if events[3] < 0.5 and all(events[i] < 0.5 for i in range(4, 7)):
        print(3)  # ExamineAirway
        continue
    if any(events[i] > 0.5 for i in [4, 5, 6]):
        print(36)  # PerformHeadTiltChinLift
        continue

    # Breathing management
    if events[7] > 0.5:
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[1] > 0 and measured_values[1] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation management
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check other vitals and assess stability
    airway_clear = events[3] > 0.5 or events[0] > 0.5  # AirwayClear or ResponseVerbal
    breathing_stable = (measured_times[1] > 0 and measured_values[1] >= 8) and (measured_times[5] > 0 and measured_values[5] >= 88)
    circulation_stable = measured_times[4] > 0 and measured_values[4] >= 60

    if airway_clear and breathing_stable and circulation_stable:
        print(48)  # Finish
        break

    # If vital signs not clear or measurements outdated, proceed to monitor
    if measured_times[4] == 0 or measured_times[5] == 0 or events[3] == 0:
        print(16)  # ViewMonitor
    else:
        print(0)  # DoNothing