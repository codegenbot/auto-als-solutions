airway_checked = False
breathing_checked = False
circulation_checked = False
disability_checked = False
exposure_checked = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life threats
    if (
        measured_times[5] > 0
        and measured_values[5] < 65
        or measured_times[4] > 0
        and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # A: Airway Assessment
    if not airway_checked or events[3] + events[4] + events[5] < 0.5:
        print(3)  # ExamineAirway
        airway_checked = True
        continue

    # B: Breathing Assessment
    if not breathing_checked:
        if events[7] > 0.5 or (measured_times[6] > 0 and measured_values[6] < 8):
            print(29)  # UseBagValveMask
            breathing_checked = True
            continue
        else:
            print(4)  # ExamineBreathing
            breathing_checked = True
            continue

    # C: Circulation Assessment
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # D: Disability (Neurological) Assessment
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # E: Exposure Assessment
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Reassess or stabilize
    print(16)  # ViewMonitor or other stabilization action

    # Check for stabilization
    stabilized = (
        (measured_times[5] > 0 and measured_values[5] >= 88)
        and (measured_times[6] > 0 and measured_values[6] >= 8)
        and (measured_times[4] > 0 and measured_values[4] >= 60)
    )
    if stabilized:
        print(48)  # Finish
        break