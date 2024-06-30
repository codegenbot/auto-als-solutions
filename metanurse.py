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

    if events[3] > 0:  # AirwayClear
        airway_confirmed = True
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    if len(events) > 12 and events[12] > 0:  # some valid breathing measurement or event
        breathing_assessed = True
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        continue

    if measured_times[4] > 0 and measured_values[4] > 60:  # valid MAP check
        circulation_checked = True
    if not circulation_checked:
        print(5)  # ExamineCirculation
        continue

    if not disability_checked:  # assuming we perform a disability check
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    if not exposure_checked:  # assuming we perform an exposure check
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
        initial_assessments_done = True

    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue

    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    if initial_assessments_done:
        if (
            (measured_times[5] > 0 and measured_values[5] >= 88)
            and (measured_times[6] > 0 and measured_values[6] >= 8)
            and (measured_times[4] > 0 and measured_values[4] >= 60)
        ):
            print(48)  # Finish
            break

    if not satsProbeUsed and (measured_times[5] == 0 or measured_values[5] < 88):
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue
    print(16)  # ViewMonitor