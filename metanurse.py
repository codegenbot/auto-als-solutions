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

    if events[7] > 0 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)
        continue

    if not airway_confirmed:
        print(3)
        if events[3] > 0:
            airway_confirmed = True
            continue

    if not breathing_assessed and airway_confirmed:
        print(4)
        if not satsProbeUsed:
            print(25)
            satsProbeUsed = True
            continue
        breathing_assessed = True
        continue

    if not circulation_checked and breathing_assessed:
        print(27)
        bpCuffUsed = True
        print(5)
        circulation_checked = True
        continue

    if not disability_checked and circulation_checked:
        print(6)
        disability_checked = True
        continue

    if not exposure_checked and disability_checked:
        print(7)
        exposure_checked = True
        initial_assessments_done = True
        continue

    if (
        airway_confirmed
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)
        break

    print(0)