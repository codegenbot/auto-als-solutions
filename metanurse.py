airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
                airway_confirmed = True
            else:
                print(3)
                continue

        if not breathing_assessed:
            if measured_times[5] == 0 or measured_values[5] < 88:
                if not satsProbeUsed:
                    print(19)
                    satsProbeUsed = True
                    continue
                print(25)
                continue
            breathing_assessed = True

        if not circulation_checked:
            print(5)
            continue

        if not disability_checked:
            print(6)
            continue

        initial_assessments_done = True

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)
        continue

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

    print(0)