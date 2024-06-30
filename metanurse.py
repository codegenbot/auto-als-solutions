airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
satsProbeUsed = False
initial_assessments_done = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue
        
        if not breathing_assessed:
            if events[12] > 0.1 or events[13] > 0.1 or events[14] > 0.1:
                breathing_assessed = True
                print(19)  # OpenBreathingDrawer
                print(25)  # UseSatsProbe
                print(16)  # ViewMonitor
                satsProbeUsed = True
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

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    if initial_assessments_done:
        if measured_times[5] == 0 or measured_values[5] < 88:
            if not satsProbeUsed:
                print(19)  # OpenBreathingDrawer
                print(25)  # UseSatsProbe
                satsProbeUsed = True
            else:
                print(30)  # UseNonRebreatherMask
            continue
        
        if measured_times[4] == 0 or measured_values[4] < 60:
            print(27)  # UseBloodPressureCuff
            continue

        if (measured_times[5] > 0 and measured_values[5] >= 88 and 
            measured_times[6] > 0 and measured_values[6] >= 8 and
            measured_times[4] > 0 and measured_values[4] >= 60):
            print(48)  # Finish
            break