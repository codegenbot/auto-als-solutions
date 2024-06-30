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

    if events[7]:  # BreathingNone detected
        print(29)  # UseBagValveMask
        continue
    
    if events[17]:  # No radial pulse palpable
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3]:  # AirwayClear
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue

        if not breathing_assessed:
            if events[12] or events[13] or events[14]:  # Any breathing abnormalities
                breathing_assessed = True
                print(25) if not satsProbeUsed else print(16)  # UseSatsProbe initially, then ViewMonitor
                satsProbeUsed = True
                continue
            else:
                print(4)  # ExamineBreathing
                continue

        if not circulation_checked:
            if events[16] > 0.1:  # RadialPulsePalpable
                circulation_checked = True
            else:
                print(5)  # ExamineCirculation
                continue

        if not disability_checked:
            if events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1:  # AVPU responses
                disability_checked = True
            else:
            print(6)  # ExamineDisability
            continue

        if not exposure_checked:
            exposure_checked = True
            print(7)  # ExamineExposure
            continue

        initial_assessments_done = True

    if initial_assessments_done:
        if all([measured_times[5] and measured_values[5] >= 88, 
                measured_times[6] and measured_values[6] >= 8, 
                measured_times[4] and measured_values[4] >= 60]):
            print(48)  # Finish
            break

        else:
            if not satsProbeUsed or measured_values[5] < 88:
                print(25)  # UseSatsProbe
                satsProbeUsed = True
                continue

            if measured_values[4] < 60:
                print(27)  # UseBloodPressureCuff
                continue