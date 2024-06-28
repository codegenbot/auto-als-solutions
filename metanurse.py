while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)
        continue

    if events[3] < 0.5 and all(events[i] < 0.5 for i in range(4, 7)):
        print(3)
        continue

    if events[7] > 0.5:
        print(29)
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)
        continue
    
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)
        continue

    stable_conditions = (
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60
    )
    if stable_conditions:
        print(48)
        break

    print(16)