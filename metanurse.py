steps = 0
airway_confirmed = False
breathing_confirmed = False
circulation_confirmed = False
disability_confirmed = False
exposure_confirmed = False
sats_probe_used = False

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    airway_clear = events[3] > 0.1

    if not airway_confirmed:
        print(3)  # ExamineAirway
        airway_confirmed = True
        continue

    if not breathing_confirmed:
        if not sats_probe_used:
            print(19)  # OpenBreathingDrawer
            print(25)  # UseSatsProbe
            sats_probe_used = True
            continue
        print(4)  # ExamineBreathing
        breathing_confirmed = True
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not circulation_confirmed:
        print(5)  # ExamineCirculation
        circulation_confirmed = True
        continue

    if not disability_confirmed:
        print(6)  # ExamineDisability
        disability_confirmed = True
        continue

    if not exposure_confirmed:
        print(7)  # ExamineExposure
        exposure_confirmed = True
        continue

    if measured_times[5] == 0 or measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing