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
    if not airway_checked or events[3] + events[4] + events[5] > 0:
        airway_checked = True
        if events[4] > 0 or events[5] > 0:  # Vomit or Blood blocking airways
            print(31)  # UseYankeurSuctionCatheter
        else:
            print(3)  # ExamineAirway
        continue
    
    # B: Breathing Assessment
    if not breathing_checked:
        breathing_checked = True
        if events[7] > 0:  # BreathingNone event is triggered
            print(29)  # UseBagValveMask
        else:
            print(4)  # ExamineBreathing
        continue

    # C: Circulation Assessment
    if not circulation_checked:
        circulation_checked = True
        print(5)  # ExamineCirculation
        continue

    # D: Disability (Neurological) Assessment
    if not disability_checked:
        disability_checked = True
        print(6)  # ExamineDisability
        continue

    # E: Exposure Assessment
    if not exposure_checked:
        exposure_checked = True
        print(7)  # ExamineExposure
        continue

    # Reassessments and final checks
    if events[15] > 0.5:  # Recheck ventricular resistance issues
        print(16)  # ViewMonitor
        continue

    # Check for stabilization
    stabilized = (
        (measured_times[5] > 0 and measured_values[5] >= 88)
        and (measured_times[6] > 0 and measured_values[6] >= 8)
        and (measured_times[4] > 0 and measured_values[4] >= 60)
    )
    if stabilized:
        print(48)  # Finish
        break

    # Default action if not stabilized and no other examinations
    print(16)  # ViewMonitor