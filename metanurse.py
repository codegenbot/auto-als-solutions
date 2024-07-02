airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
sats_probe_used = False
bp_cuff_used = False
steps = 0
critical_condition_active = False

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
        critical_condition_active = True
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.01:  # AirwayClear is confirmed
                airway_confirmed = True
            print(3)  # ExamineAirway
            continue

        if not breathing_assessed and airway_confirmed:
            if events[12] > 0.01:  # BreathingEqualChestExpansion is confirmed
                breathing_assessed = True
            print(4)  # ExamineBreathing
            continue

        if not circulation_checked and breathing_assessed:
            if events[16] > 0.01 or events[17] > 0.01:  # Circulation status updated
                circulation_checked = True
            print(5)  # ExamineCirculation
            continue

        if not disability_checked and circulation_checked:
            if (
                events[21] > 0.01 or events[22] > 0.01 or events[23] > 0.01
            ):  # Disability checked
                disability_checked = True
            print(6)  # ExamineDisability
            continue

        if not exposure_checked and disability_checked:
            exposure_checked = True
            initial_assessments_done = True
            print(7)  # ExamineExposure
            continue

    if not sats_probe_used:
        print(25)  # UseSatsProbe
        sats_probe_used = True
        continue

    if (measured_times[5] > 0 and measured_values[5] < 88) or critical_condition_active:
        print(30)  # UseNonRebreatherMask
        continue

    if not bp_cuff_used and circulation_checked:
        print(27)  # UseBloodPressureCuff
        bp_cuff_used = True
        continue

    if measured_times[4] != 0 and measured_values[4] < 60:
        print(38)  # TakeBloodPressure
        continue

    if (
        initial_assessments_done
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing as a fallback