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

    # Immediate critical responses
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if events[7] > 0.1 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Airway Evaluation
    if not airway_confirmed:
        if events[3] > 0.1:  # AirwayClear
            airway_confirmed = True
        elif events[4] > 0.1 or events[5] > 0.1:  # AirwayVomit or AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
            continue
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing Evaluation
    if not breathing_assessed:
        if events[8] > 0.1 or events[9] > 0.1 or events[13] > 0.1:  # Breathing issues
            print(29)  # UseBagValveMask
            continue
        breathing_assessed = True
        print(4)  # ExamineBreathing
        continue

    # Circulation Evaluation
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Disability Evaluation
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Exposure Evaluation
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Handling Treatment
    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if not monitorViewed:
        print(16)  # ViewMonitor
        monitorViewed = True
        continue

    # Treatment based on oxygen saturation and blood pressure monitoring
    if measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    # If conditions are stable and all checked
    if measured_times[5] > 0 and measured_values[5] >= 88 and measured_times[6] > 0 and measured_values[6] >= 8 and measured_times[4] > 0 and measured_values[4] >= 60:
        print(48)  # Finish
        break

    # Default action
    print(0)  # DoNothing