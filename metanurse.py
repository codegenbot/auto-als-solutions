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
            if events[12] > 0 or events[13] > 0 or events[14] > 0:
                breathing_assessed = True
            else:
                print(4)  # ExamineBreathing
                continue
        
        if not satsProbeUsed:
            print(19)  # OpenBreathingDrawer
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            continue

        if len([m for m, v in zip(measured_times[0:3], measured_values[0:3]) if m > 0 and v]) > 0:
            circulation_checked = True
        
        if not disability_checked:
            if events[21] > 0 or events[22] > 0 or events[23] > 0:
                disability_checked = True
            else:
                print(6)  # ExamineDisability
                continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Handle Breathing
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Handle Circulation
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        print(38)  # TakeBloodPressure
        continue

    # Finishing condition
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and exposure_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing