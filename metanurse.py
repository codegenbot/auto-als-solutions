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

    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1:
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue
        if not breathing_assessed:
            if events[9] > 0:
                breathing_assessed = True
            else:
                print(4)  # ExamineBreathing
                continue
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
    else:
        if not satsProbeUsed:
            print(19)  # OpenBreathingDrawer
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue
        if measured_times[4] == 0 or measured_values[4] < 60:
            print(14)  # UseVenflonIVCatheter
            continue
        if measured_times[5] == 0 or measured_values[5] < 88:
            print(16)  # ViewMonitor