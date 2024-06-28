step_count = 0
airway_checked = False
breathing_checked = False
circulation_checked = False
disability_checked = False
exposure_checked = False
sat_probe_used = False
bp_cuff_used = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate action if critical condition detected
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Regular checks if needed
    if not airway_checked:
        print(3)  # ExamineAirway
        airway_checked = True
        continue

    if not breathing_checked:
        print(4)  # ExamineBreathing
        breathing_checked = True
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
        exposurec_checked = True
        continue

    if not sat_probe_used:
        print(25)  # UseSatsProbe
        sat_probe_used = True
        continue

    if not bp_cuff_used:
        print(27)  # UseBloodPressureCuff
        bp_cuff_used = True
        continue

    # Update regular monitoring
    print(16)  # ViewMonitor

    # React to measurements
    if measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
    elif measured_values[6] < 8:
        print(29)  # UseBagValveMask
    elif measured_values[4] < 60:
        print(15)  # GiveFluids

    # Check if conditions to finish are met
    all_good = (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    )

    if all_good and step_count > 10:
        print(48)  # Finish
        break

    step_count += 1