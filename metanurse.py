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
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)
        continue
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)
        continue
    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1:
                airway_confirmed = True
            else:
                print(3)
                continue
        if not breathing_assessed:
            if events[10] > 0.1:
                breathing_assessed = True
            else:
                print(4)
                continue
        if not circulation_checked:
            if events[16] > 0.1:
                circulation_checked = True
            else:
                print(5)
                continue
        if not disability_checked:
            print(6)
            disability_checked = True
            continue
        if not exposure_checked:
            print(7)
            exposure_checked = True
            continue
        initial_assessments_done = True
    if not satsProbeUsed:
        print(25)
        satsProbeUsed = True
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
    else:
        print(16)