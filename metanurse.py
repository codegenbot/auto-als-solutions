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
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        if events[3] > 0.7:
            airway_confirmed = True
        print(3)  # ExamineAirway
        continue

    if not breathing_assessed:
        if not satsProbeUsed:
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue
        if measured_times[5] > 0 and measured_values[5] >= 88:
            breathing_assessed = True
        print(4)  # ExamineBreathing
        continue

    if not circulation_checked:
        if measured_times[4] > 0 and measured_values[4] >= 60:
            circulation_checked = True
        else:
            print(27)  # UseBloodPressureCuff
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and exposure_checked
    ):
        print(48)  # Finish
        break