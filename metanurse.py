airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
sats_used = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    if events[7] == 1.0 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        continue

    if events[3] > 0:
        airway_confirmed = True

    if events[12] > 0 or events[13] > 0:
        breathing_assessed = True

    if not sats_used and measured_times[5] == 0:
        print(25)  # UseSatsProbe
        sats_used = True
        continue

    if not circulation_checked:
        print(5)  # ExamineCirculation
        if events[16] > 0 or events[17] > 0:
            circulation_checked = True
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    if measured_times[5] == 0 or measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    if measured_times[6] == 0 or measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break