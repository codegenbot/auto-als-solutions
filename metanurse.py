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
        print(29)  # UseBagValveMask for no breathing
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression for critical conditions
        continue

    if not airway_confirmed:
        if events[3] > 0:  # AirwayClear
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway if not confirmed
            continue

    if not breathing_assessed:
        if measured_times[5] == 0 or measured_values[5] < 88:
            print(25)  # UseSatsProbe if not assessed or below 88%
            continue
        breathing_assessed = True

    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True  # Adjust this when you know circulation status
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
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish if all conditions are met
        break

    print(0)  # DoNothing as a default action