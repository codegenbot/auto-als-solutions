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

    # Critical breathing issue
    if events[7] > 0.5:  # BreathingNone has occurred
        print(29)  # UseBagValveMask
        continue

    # Regular checks
    if not airway_checked:
        print(3)  # ExamineAirway
        airway_checked = True
    elif not breathing_checked:
        print(4)  # ExamineBreathing
        breathing_checked = True
    elif not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
    elif not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
    elif not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
    else:
        # Reassess or stabilize further or end the scenario
        stabilized = (
            (measured_times[5] > 0 and measured_values[5] >= 88)
            and (measured_times[6] > 0 and measured_values[6] >= 8)
            and (measured_times[4] > 0 and measured_values[4] >= 60)
        )
        if stabilized:
            print(48)  # Finish
            break
        else:
            print(16)  # ViewMonitor or other stabilization action