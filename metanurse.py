airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
monitorViewed = False
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
        print(17)  # StartChestCompression
        continue

    # Check and stabilize airway
    if not airway_confirmed:
        if events[3] > 0.1:
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Check and stabilize breathing
    if not breathing_assessed:
        if events[12] > 0 or events[13] > 0 or events[14] > 0:
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
            continue

    # Check and stabilize circulation
    if not circulation_checked:
        if events[16] > 0 or events[17] > 0:
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    # Check disability status
    if not disability_checked:
        if events[21] > 0 or events[22] > 0 or events[23] > 0:
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

    # Check for exposure
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    initial_assessments_done = True

    if not satsProbeUsed:
        print(19)  # OpenBreathingDrawer
        satsProbeUsed = True
        continue

    if not monitorViewed:
        print(25)  # UseSatsProbe
        monitorViewed = True
        continue

    if measured_times[5] > 0 and measured_values[5] >= 88:
        if measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue

    if measured_times[4] > 0 and measured_values[4] >= 60:
        if measured_values[4] < 60:
            print(27)  # UseBloodPressureCup
            print(38)  # TakeBloodPressure
            continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and exposure_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing