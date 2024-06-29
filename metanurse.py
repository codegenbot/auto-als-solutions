airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_assessed = False
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
            if events[3] > 0.1:  # AirwayClear is higher than threshold
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue
        elif not breathing_assessed:
            if events[9] > 0:  # BreathingSeeSaw is higher than threshold
                breathing_assessed = True
            else:
                print(4)  # ExamineBreathing
                continue
        elif not circulation_checked:
            if events[16] > 0:  # RadialPulsePalpable is present
                circulation_checked = True
            else:
                print(5)  # ExamineCirculation
                continue
        elif not disability_checked:
            if events[21] > 0 or events[22] > 0:  # Check AVPU responses
                disability_checked = True
            else:
                print(6)  # ExamineDisability
                continue
        else:
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

    if not measured_times[5] > 0 or measured_values[5] < 88:
        if not satsProbeUsed:
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue
        else:
            print(16)  # ViewMonitor
            continue
    elif not measured_times[4] > 0 or measured_values[4] < 60:
        print(14)  # UseVenflonIVCatheter
        print(15)  # GiveFluids
    else:
        print(16)  # ViewHubonitor