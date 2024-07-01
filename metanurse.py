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

    if steps == 1:
        print(19)  # OpenBreathingDrawer
        continue
    if steps == 2:
        print(25)  # UseSatsProbe
        continue

    # Critical immediate actions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not satsProbeUsed and measured_times[5] > 0:
        satsProbeUsed = True
        if measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue

    # Systematic ABCDE Check
    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            if events[3] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
                airway_confirmed = True
                if events[4] > 0.1 or events[5] > 0.1:
                    print(31)  # UseYankeurSuctionCatheter
                    continue
            continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            if events[8] > 0.1 or events[14] > 0.1:
                breathing_assessed = True
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            if events[16] > 0.1 or events[17] > 0.1:
                circulation_checked = True
            continue

        if not disability_checked:
            print(8)  # ExamineResponse
            if events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1:
                disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Continue monitoring until stable
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

    # Default action
    print(0)  # DoNothing as last resort