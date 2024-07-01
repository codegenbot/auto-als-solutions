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

    # Immediate life-threatening conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue
    if events[7] >= 0.7:  # BreathingNone very high
        print(29)  # UseBagValveMask
        continue

    # ABCDE Protocol
    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            continue
        if not breathing_assessed:
            print(4)  # ExamineBreathing
            continue
        if not circulation_checked:
            print(5)  # ExamineCirculation
            continue
        if not disability_checked:
            print(6)  # ExamineDisability
            continue
        if not exposure_checked:
            print(7)  # ExamineExposure
            continue
        # Only mark as done if all are checked
        initial_assessments_done = (
            airway_confirmed
            and breathing_assessed
            and circulation_checked
            and disability_checked
            and exposure_checked
        )

    # Using necessary equipment to gather vital data
    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if not bpCuffUsed:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    # Assess and act based on measurements
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Ending condition after ensuring stabilization
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_values[6] >= 8
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default action if no other action is taken
    print(0)  # DoNothing