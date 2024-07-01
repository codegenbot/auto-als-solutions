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

    if "breathing drawer" in observations and not monitorViewed:
        print(19)
        continue

    if "breathing drawer" in observations and not satsProbeUsed:
        print(25)
        satsProbeUsed = True
        monitorViewed = True
        continue

    if not airway_confirmed:
        print(3)
        airway_confirmed = True
        continue

    if not breathing_assessed:
        print(4)
        breathing_assessed = True
        continue

    if not monitorViewed:
        print(16)
        monitorViewed = True
        continue

    if (
        [
            airway_confirmed,
            breathing_assessed,
            circulation_checked,
            disability_checked,
            exposure_checked,
        ].count(True)
        == 5
        and (measured_times[5] == 0 or measured_values[5] >= 88)
        and (measured_times[6] == 0 or measured_values[6] >= 8)
        and (measured_times[4] == 0 or measured_values[4] >= 60)
    ):
        print(48)
        break

    print(0)