step = 0
airway_checked = False
breathing_checked = False
circulation_checked = False
disability_checked = False
exposure_checked = False
sats_probed = False
bp_cuffed = False
stabilized = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Determine immediate critical conditions
    critical_sats = measured_times[5] > 0 and measured_values[5] < 65
    critical_map = measured_times[4] > 0 and measured_values[4] < 20

    if critical_sats or critical_map:
        print(17)  # StartChestCompression
        continue

    # Assess if stabilized
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        stabilized = True

    if stabilized:
        print(48)  # Finish
        break

    # Rotate through checks to update patient status comprehensively
    if step % 5 == 0:
        if not airway_checked or events[3] + events[4] + events[5] + events[6] == 0:
            print(3)  # ExamineAirway
            airway_checked = True
    elif step % 5 == 1:
        if not breathing_checked:
            print(4)  # ExamineBreathing
            breathing_checked = True
    elif step % 5 == 2:
        if not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
    elif step % 5 == 3:
        if not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
    elif step % 5 == 4:
        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True

    # Utilize monitoring tools after initial checks
    if step >= 5 and not sats_probed:
        print(25)  # UseSatsProbe
        sats_probed = True
    elif step >= 6 and not bp_cuffed:
        print(27)  # UseBloodPressureCuff
        bp_cuffed = True
    else:
        print(16)  # ViewMonitor

    step += 1