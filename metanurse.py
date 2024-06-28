while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    critical_airway_blocked = events[4] > 0.5 or events[5] > 0.5
    critical_no_breathing = events[7] > 0.5
    critical_low_sats = measured_times[5] > 0 and measured_values[5] < 65
    critical_low_map = measured_times[4] > 0 and measured_values[4] < 20

    if critical_low_sats or critical_low_map:
        print(17)
        continue

    if critical_airway_blocked:
        print(36)
        continue

    if measured_times[5] == 0 or measured_values[5] < 88:
        if measured_times[5] == 0:
            print(25)
        else:
            print(30)
        continue

    if measured_times[6] == 0 or measured_values[6] < 8:
        if measured_times[6] == 0:
            print(5)
        else:
            print(29)
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        if measured_times[4] == 0:
            print(27)
        else:
            print(15)
        continue

    if measured_times[0] == 0:
        print(2)
        continue

    stabilised = (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    )

    if stabilised:
        print(48)
        break

    print(16)