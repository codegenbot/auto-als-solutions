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

    critical_sat = measured_times[5] > 0 and measured_values[5] < 65
    critical_map = measured_times[4] > 0 and measured_values[4] < 20

    if critical_sat or critical_map:
        print(17)  # StartChestCompression
        continue

    if not satsProbeUsed and measured_times[5] == 0:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if not bpCuffUsed and measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            if events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:
                airway_confirmed = True
            continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    if measured_values[5] < 88 and measured_times[5] > 0:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_values[6] < 8 and measured_times[6] > 0:
        print(29)  # UseBagValveMask
        continue

    if measured_values[4] < 60 and measured_times[4] > 0:
        print(15)  # GiveFluids
        continue

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

    print(0)  # DoNothing as last resort