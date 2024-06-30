airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False
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
            if events[3] > 0.1:
                airway_confirmed = True
            else:
                print(3)
                continue

        if not breathing_assessed:
            if events[12] > 0 or events[13] > 0 or events[14] > 0:
                breathing_assessed = True
            else:
                if not satsProbeUsed:
                    print(25)
                    satsProbeUsed = True
                    continue
                else:
                    print(16)
                    continue

        if not circulation_checked:
            if events[16] > 0 or events[17] > 0:
                circulation_checked = True
            else:
                print(5)
                continue

        if not disability_checked:
            if events[21] > 0 or events[22] > 0 or events[23] > 0:
                disability_checked = True
            else:
                print(6)
                continue

        if not exposure_checked:
            print(7)
            exposure_checked = True
            continue

        initial_assessments_done = True

    if initial_assessments_done:
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

        if not satsProbeUsed:
            print(25)
            satsProbeUsed = True
            continue

        if not bpCuffUsed:
            print(27)
            bpCuffUsed = True
            continue

        if measured_times[5] == 0 or measured_values[5] < 88:
            print(30)
            continue

        if measured_times[4] == 0 or measured_values[4] < 60:
            print(27)
            continue

        if measured_times[6] == 0 or measured_values[6] < 8:
            print(29)
            continue