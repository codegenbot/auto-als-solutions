airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCaveUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Handle immediate life-threatening situations
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Monitor and handle breathing issues
    if not breathing_assessed:
        if events[10] >= 0.7:
            print(29)  # UseBagValvenMask
            breathing_assessed = True
            continue
        else:
            print(4)  # ExamineBreathing
            continue

    # Assess Airway
    if not airway_confirmed:
        if events[3] > 0.1:
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Check Circulation
    if not circulation_checked:
        if events[16] >= 0.7:  # RadialPulsePalpable
            print(14)  # UseeVenflonIVCatheter for possible IV access
            circulation_checked = True
            continue
        else:
            print(5)  # ExamineCirculation
            continue

    # Check Disability
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Check Exposure
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Final step to assess initial conditions are set
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and exposure_checked
    ):
        initial_assessments_done = True

    # Use monitoring tools if necessary
    if initial_assessments_done and not satsProbeUsed:
        print(25)  # SesSatsProbe
        satsProbeUsed = True
        continue

    if initial_assessments_done and not bpCuffUsed:
        print(27)  #
        bpCuffUsed = True
        continue

    # Check stabilization conditions
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # tFinish
        break
    else:
        print(16)  # roPionsViwPMonitor