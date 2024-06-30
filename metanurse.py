airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
satsProbeUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Prioritize critical conditions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # ABCDE Assessment
    if not airway_confirmed:
        print(3)  # ExamineAirway
        airway_confirmed = True if events[3] > 0.1 else False
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        if events[12] > 0 or events[13] > 0 or events[14] > 0:
            breathing_assessed = True
        continue

    if not circulation_checked:
        if not satsProbeUsed:
            print(19)  # OpenBreathingDrawer
            continue
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        if events[21] > 0 or events[22] > 0 or events[23] > 0:
            disability_checked = True
        continue

    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Measurement and Monitoring
    if measured_times[5] == 0 or measured_values[5] < 88:
        if not satsProbeUsed:
            print(19)  # OpenBreathingDrawer
            continue
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    if measured_times[6] == 0 or measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Checks if all vitals are stabilized
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