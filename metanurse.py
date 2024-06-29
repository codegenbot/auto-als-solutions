airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False
steps = 0

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if not airway_confirmed:
        print(3)
        continue

    if not breathing_assessed and airway_confirmed:
        print(4)
        continue

    if not circulation_checked and breathing_assessed:
        print(5)
        continue

    if not disability_checked and circulation_checked:
        print(6)
        continue

    if steps >= 350:
        print(48)
        break

    if events[7] >= 0.7:
        print(29)
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)
        continue

    if events[3] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
        airway_confirmed = True

    if events[10] > 0.1:
        breathing_assessed = True

    if events[16] > 0.1 or events[17] > 0.1:
        circulation_checked = True

    if events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1:
        disability_checked = True

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
        if (
            measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
            and measured_times[4] > 0
            and measured_values[4] >= 60
        ):
            print(48)
            break
        else:
            print(16)
            continue

    print(0)
    steps += 1