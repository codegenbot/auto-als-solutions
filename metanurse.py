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

    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        airway_confirmed = True  # Assume airway check done
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True  # Assume breathing check done
        continue

    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True  # Assume circulation check done
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True  # Assume disability check done
        continue

    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True  # Assume exposure check done
        continue

    initial_assessments_done = (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and exposure_checked
    )

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

    if not bpCuffUsed:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    print(0)  # DoNothing as last resort