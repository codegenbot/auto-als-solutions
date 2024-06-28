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
            last_action = 17
            print(17)  # StartChestCompression
            continue

    # Check Airway
    if (
        events[3] < 0.5 and events[4] < 0.5 and events[5] < 0.5 and events[6] < 0.5
    ) or critical_airway_blocked:
        if last_action != 3:
            last_action = 3
            print(3)  # ExamineAirway
            continue

    # Check Breathing
    if critical_no_breathing:
        if last_action != 29:
            last_action = 29
            print(29)  # UseBagValveMask
            continue

    # Check oxygen saturation and respiratory rate
    if measured_times[5] > 0 and measured_values[5] < 88:
        if last_action != 30:
            last_action = 30
            print(30)  # UseNonRebreatherMask
            continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        if last_action != 29:
            last_action = 29
            print(29)  # UseBagValveMask
            continue

    # Check Circulation
    if measured_times[4] > 0 and measured_values[4] < 60:
        if last_action != 15:
            last_action = 15
            print(15)  # GiveFluids
            continue

    # If there are enough observations to conclude the patient is stabilized, finish the scenario
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        if last_action != 48:
            last_action = 48
            print(48)  # Finish
            break

    # Default action to gather more information
    if last_action != 16:
        last_action = 16
        print(16)  # ViewMonitor