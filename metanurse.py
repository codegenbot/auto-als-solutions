airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
saturation_measured = False
steps = 0

while steps < 350:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        steps += 1
        continue

    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            steps += 1
            continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        if not saturation_measured:
            print(25)  # UseSatsProbe
            saturation_measured = True
            steps += 1
            continue
        print(30)  # UseNonRebreatherMask
        steps += 1
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        steps += 1
        continue

    if not circulation_checked:
        if events[17] > 0.5:  # RadialPulseNonPalpable
            print(5)  # ExamineCirculation
            circulation_checked = True
            steps += 1
            continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        steps += 1
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        steps += 1
        continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor
    steps += 1