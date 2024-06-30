airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
satsProbeUsed = False
monitorViewed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical actions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Respond to hint for finger probe and monitoring
    if not breathing_assessed or not satsProbeUsed or not monitorViewed:
        if not breathing_assessed:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue
        elif not satsProbeUsed:
            print(19)  # OpenBreathingDrawer
            satsProbeUsed = True
            continue
        elif not monitorViewed:
            print(25)  # UseSatsProbe
            print(16)  # ViewMonitor
            monitorViewed = True
            continue

    # Examine Airway
    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0.1:
            airway_confirmed = True
        continue

    # Examine Circulation
    if not circulation_checked:
        print(5)  # ExamineCirculation
        if events[16] > 0 or events[17] > 0:
            circulation_checked = True
        continue

    # Examine Disability
    if not disability_checked:
        print(6)  # ExamineDisability
        if events[21] > 0 or events[22] > 0 or events[23] > 0:
            disability_checked = True
        continue

    # Examine Exposure
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
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