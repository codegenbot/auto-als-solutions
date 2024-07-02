steps = 0
airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
sats_probe_used = False
bp_cuff_used = False
monitor_viewed_after_sats_probe = False
monitor_viewed_after_bp_cuff = False

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if events[3] > 0:
        airway_confirmed = True

    if events[7] > 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
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

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            breathing_assessed = True
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
            initial_assessments_done = True
            continue

    if initial_assessments_done:
        if not sats_probe_used:
            print(25)  # UseSatsProbe
            sats_probe_used = True
            monitor_viewed_after_sats_probe = False
            continue

        if sats_probe_used and not monitor_viewed_after_sats_probe:
            print(16)  # ViewMonitor
            monitor_viewed_after_sats_probe = True
            continue

        if not bp_cuff_used:
            print(27)  # UseBloodPressureCuff
            bp_cuff_used = True
            monitor_viewed_after_bp_cuff = False
            continue

        if bp_cuff_used and not monitor_viewed_after_bp_cuff:
            print(16)  # ViewMonitor
            monitor_viewed_after_bp_cuff = True
            continue

        if measured_times[5] > 0 and measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
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

    print(0)  # DoNothing as last resort