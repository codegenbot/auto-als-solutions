steps = 0

airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
sats_checked = False

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Handle critical conditions immediately
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Initialize the Sats probe usage if not done
    if not satsProbeUsed:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # View monitor readings after using the Sats probe
    if satsProbeUsed and not sats_checked:
        print(16)  # ViewMonitor
        sats_checked = True
        continue

    # Checking for severe conditions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Sequential ABCDE Assessments
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

    # Check if stabilized
    if initial_assessments_done and (
        (measured_times[5] > 0 and measured_values[5] >= 88)
        and (measured_times[6] > 0 and measured_values[6] >= 8)
        and (measured_times[4] > 0 and measured_values[4] >= 60)
    ):
        print(48)  # Finish
        break

    # Ensure vital parameters are being measured continuously
    if not sats_checked:
        print(25)  # UseSatsProbe
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue