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

    if not airway_confirmed:
        if events[3] > 0:  # AirwayClear
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    if not breathing_assessed:
        if measured_times[5] > 0 and measured_values[5] >= 88:  # Breathing status check
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
            continue

    if not circulation_checked:
        if (
            measured_times[4] > 0 and measured_values[4] >= 60
        ):  # Circulation status check
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    if not disability_checked:
        if (
            measured_times[0] > 0 or measured_times[2] > 0
        ):  # Check if AVPU info available
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

    if not exposure_checked:
        if events[26] > 0:  # ExposureRash, simple example
            exposure_checked = True
        else:
            print(7)  # ExamineExposure
            continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and exposure_checked
    ):
        initial_assessments_done = True

    if initial_assessments_done:
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

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # If all metrics are not critical but assessment is not complete
    print(16)  # ViewMonitor