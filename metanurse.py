airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False
critical_condition_encountered = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().strip().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not critical_condition_encountered:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            if events[3] > 0:  # AirwayClear
                airway_confirmed = True
            continue

        if not breathing_assessed and airway_confirmed:
            if events[11] > 0 or events[12] > 0 or events[14] > 0:  # Breathing issues
                breathing_assessed = True
                print(29)  # UseBagValveMask
                continue
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

        if not circulation_checked and breathing_assessed:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        if not disability_checked and circulation_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if not exposure_checked and disability_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            initial_assessments_done = True
            continue

    if not satsProbeUsed and breathing_assessed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if not bpCuffUsed and circulation_checked:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
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