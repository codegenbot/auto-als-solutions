airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False
steps = 0

while steps < 350:
    steps += 1

    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue

    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    if events[3] > 0:
        airway_confirmed = True

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        continue

    if events[6] > 0 or events[7] > 0:
        print(29)  # UseBagValveMask
        continue
    else:
        breathing_assessed = True

    if not circulation_checked:
        print(5)  # ExamineCirculation
        continue

    if events[16] > 0:
        circulation_checked = True
    elif events[17] > 0:
        print(15)  # GiveFluids
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        continue

    disability_checked = True

    if not exposure_checked:
        print(7)  # ExamineExposure
        continue

    exposure_checked = True
    initial_assessments_done = True

    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if not bpCuffUsed:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if (
        initial_assessments_done
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing as last resort