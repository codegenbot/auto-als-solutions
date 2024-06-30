airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
sats_probe_used = False
saturation_checked = False
blood_pressure_checked = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check vital signs if observed
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue

    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue
    
    # Initial assessments
    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0:
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

        if not saturation_checked and not sats_probe_used:
            print(25)  # UseSatsProbe
            sats_probe_used = True
            continue

        if not circulation_checked:
            if events[16] > 0 or events[17] > 0:
                circulation_checked = True
            else:
                print(5)  # ExamineCirculation
                continue

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

    # Direct treatment based on assessments
    if measured_times[5] == 0 or measured_values[5] < 88 and sats_probe_used:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        if not blood_pressure_checked:
            print(27)  # UseBloodPressureCuff
            blood_pressure_checked = True
            continue

    # Verification for stabilization
    if (measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60):
        print(48)  # Finish
        break

    # Default action if nothing is applied
    print(0)  # DoNothing if conditions not met to do anything specific