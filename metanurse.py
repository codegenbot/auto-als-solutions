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

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0:  # AirwayClear
            airway_confirmed = True
        elif events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
            continue

    elif not breathing_assessed:
        print(4)  # ExamineBreathing
        if not satsProbeUsed and (measured_times[5] == 0 or measured_values[5] < 88):
            print(25)  # UseSatsProbe
            satsProbeUsed = True
        breathing_assessed = True

    elif not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True

    elif not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True

    elif not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True

    elif (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    else:
        print(0)  # DoNothing