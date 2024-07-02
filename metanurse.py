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

    # Immediate life-critical actions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Initial ABCDE Assessments
    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            if events[3] > 0:
                airway_confirmed = True
            continue

        if not breathing_assessed and airway_confirmed:
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
            initial_assessorts_done = True
            continue

    # Progressive Intervenions
    if not satsProbeUsed and breathing_assessed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if not bpCuffUsed and circulation_checked:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if measured_times[4] != 0 and measured_values[4] < 60:
        print(
            15
        )  # GiveFluids, assuming using blood pressure cuff shows low MAP needing fluids
        continue

    # Check for stabilization and finish if condtions meet
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finsih
        break

    print(0)  # DoNothings as last resort