airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_examined = False
monitor_checked = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)
        continue

    if not airway_confirmed:
        if events[3] > 0:
            airway_confirmed = True
        elif any(events[i] > 0 for i in [4, 5, 6]):
            print(31)
            continue
        else:
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

    if not breathing_assessed:
        print(4)
        breathing_assessed = True
        continue

    if not circulation_checked:
        if measured_times[0] >= 0.5:
            if not monitor_checked:
                print(16)
                monitor_checked = True
                continue
            else:
                if events[17] > 0:
                    print(40)
                    continue
                else:
                    print(15)
                    continue
        else:
            print(5)
            circulation_checked = True
            continue

    if not disability_checked:
        print(6)
        disability_checked = True
        continue

    if not exposure_examined:
        print(7)
        exposure_examined = True
        continue

    if all([
        airway_confirmed, breathing_assessed, circulation_checked, 
        disability_checked, exposure_examined,
        measured_times[5] > 0, measured_values[5] >= 88,
        measured_times[6] > 0, measured_values[6] >= 8,
        measured_times[4] > 0, measured_values[4] >= 60
    ]):
        print(48)
        break

    print(16)