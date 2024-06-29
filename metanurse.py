airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
initial_assessments_done = False
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
            if events[11] > 0 and (measured_times[5] == 0 or measured_values[5] < 88):
                print(20)  # OpenBreathingDrawer
                print(25)  # UseSatsProbe
                print(16)  # ViewMonitor
                breathing_assessed = True
                continue
            else:
                print(4)  # ExamineBreathing
                continue
        if not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue
        if not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        initial_assessments_done = True
        print(7)  # ExamineExposure
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
    else:
        if measured_times[5] == 0 or measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
        elif measured_times[4] == 0 or measured_values[4] < 60:
            print(14)  # UseVenflonIVCatheter
            print(15)  # GiveFluids
        else:
            print(16)  # ViewMonitor