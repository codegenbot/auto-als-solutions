airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
initial_assessments_done = False
sats_probe_used = False
bp_cuff_used = False
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
            print(3)  # ExamineAirway
            continue
        elif not breathing_assessed:
            print(4)  # ExamineBreathing
            continue
        elif not circulation_checked:
            print(5)  # ExamineCirculation
            continue
        elif not disability_checked:
            print(6)  # ExamineDisability
            continue
        initial_assessments_done = True
        continue

    if measured_times[5] == 0 or measured_values[5] < 88:
        if not sats_probe_used:
            print(19)  # OpenBreathingDrawer
            sats_probe_used = True
            continue
        else:
            print(25)  # UseSatsProbe
            continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        if not bp_cuff_used:
            print(27)  # UseBloodPressureCuff
            bp_cuff_used = True
            continue
        else:
            print(38)  # TakeBloodPressure
            continue

    # If all is well, print "Finish" to stabilize the patient successfully
    if (
        (measured_times[5] > 0 and measured_values[5] >= 88)
        and (measured_times[6] > 0 and measured_values[6] >= 8)
        and (measured_times[4] > 0 and measured_values[4] >= 60)
    ):
        print(48)  # Finish
        break

    # Default action if no conditions are met
    print(16)  # ViewMonitor