airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
satsCheckedAfterProbe = False
drawerOpened = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical conditions leading to immediate actions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Initial ABCDE assessment
    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1:
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue

        if not breathing_assessed:
            if drawerOpened and not satsProbeUsed:
                print(25)  # UseSatsProbe
                satsProbeUsed = True
                continue

            if satsProbeUsed and not satsCheckedAfterProbe:
                print(16)  # ViewMonitor
                satsCheckedAfterProbe = True
                continue

            if events[9] > 0:
                breathing_assessed = True
            else:
                print(4)  # ExamineBreathing

        if not circulation_checked:
            if events[16] > 0 or events[17] > 0:
                circulation_checked = True
            else:
                print(5)  # ExamineCirculation
                continue

        if not disability_checked:
            if events[22] > 0:
                disability_checked = True
            else:
                print(6)  # ExamineDisability
                continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Open breathing drawer if not yet done and going for sats probe
    if not drawerOpened:
        print(19)  # OpenBreathingDrawer
        drawerOpened = True
        continue

    # Check final stabilization conditions
    if initial_assessments_done and satsCheckedAfterProbe:
        if (
            (measured_times[5] > 0 and measured_values[5] >= 88)
            and (measured_times[6] > 0 and measured_values[6] >= 8)
            and (measured_times[4] > 0 and measured_values[4] >= 60)
        ):
            print(48)  # Finish
            break