last_action = -1

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate checks for critical conditions
    critical_airway_blocked = (
        events[4] > 0.5 or events[5] > 0.5
    )  # AirwayVomit or AirwayBlood are significant
    critical_no_breathing = events[7] > 0.5  # BreathingNone
    critical_low_sats = measured_times[5] > 0 and measured_values[5] < 65
    critical_low_map = measured_times[4] > 0 and measured_values[4] < 20

    if critical_low_sats or critical_low_map:
        if last_action != 17:
            print(17)  # StartChestCompression
            last_action = 17
            continue

    # Airway Assessment
    if critical_airway_blocked or (
        events[3] < 0.5 and events[4] < 0.5 and events[5] < 0.5 and events[6] < 0.5
    ):
        if last_action != 3:
            print(3)  # ExamineAirway
            last_action = 3
            continue

    # Breathing Assessment
    if critical_no_breathing:
        if last_action != 29:
            print(29)  # UseBagValveMask
            last_action = 29
            continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        if last_action != 30:
            print(30)  # UseNonRebreatherMask
            last_action = 30
            continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        if last_action != 29:
            print(29)  # UseBagValveMask
            last_action = 29
            continue

    # Circulation Assessment
    if measured_times[4] > 0 and measured_values[4] < 60:
        if last_action != 15:
            print(15)  # GiveFluids
            last_action = 15
            continue

    # Check overall stability
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

    # Default action to gather more information
    if last_action != 16:
        print(16)  # ViewMonitor
        last_action = 16