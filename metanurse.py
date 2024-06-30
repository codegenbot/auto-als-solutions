airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
pressureCuffUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions checks
    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    # Sats probe usage check
    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # Blood pressure measurement apparatus check
    if not pressureCuffUsed:
        print(27)  # UseBloodPressureCuff
        pressureCuffUsed = True
        continue

    # Initial assessment sequences
    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1:  # AirwayClear
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue

        if not breathing_assessed:
            if events[10] > 0.1:  # EqualChestExpansion
                breathing_assessed = True
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
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExpression
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Monitoring vital check
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check for stabilization
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

    # Fallback to monitoring if unsure
    print(16)  # ViewMonitor