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

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.5:  # AirwayClear
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue
        
        if not breathing_assessed:
            if any(events[8:15]) or measured_times[1] > 0:  # Check for breathing related events
                breathing_assessed = True
            else:
                print(4)  # ExamineBreathing
                continue
                
        if not circulation_checked:
            if events[16] > 0.5 or events[17] > 0.5:  # Radial pulse palpable/non-palpable
                circulation_checked = True
            else:
                print(5)  # ExamineCirculation
                continue
                
        if not disability_checked:
            if any(events[21:24]):  # AVPU status
                disability_checked = True
            else:
:                print(6)  # ExamineDisability
                continue

        if not exposure_checked:
            exposure_checked = True
            print(7)  # ExamineExposure
            continue

        initial_assessments_done = True

    if events[7] >= 0.5 or (measured_times[6] > 0 and measured_values[6] < 8):  # extremely urgent breathing issue
        print(29)  # UseBagValveMask
        continue

    if measured_times[5] > 0 and measured_values[5] < 65:  # urgent saturation level
        print(17)  # StartChestCompression
        continue

    if measured_times[4] > 0 and measured_values[4] < 20:  # critical MAP level
        print(17)  # StartChestCompression
        continue

    if measured_times[5] == 0:
        if not satsProbeUsed:
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue
        else:
            print(19)  # OpenBreathingDrawer
            continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if (measured_times[5] > 0 and measured_values[5] >= 88) and (measured_times[6] > 0 and measured_values[6] >= 8) and (measured_times[4] > 0 and measured_values[4] >= 60):
        print(48)  # Finish
        break

    print(0)  # DoNothing as last resort