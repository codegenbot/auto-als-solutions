airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
sats_checked = False
monitor_viewed_after_probe = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving checks
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway and Breathing checks are highest priority
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    if not satsProbeUsed:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if satsProbeUsed and not monitor_viewed_after_probe:
        print(16)  # ViewMonitor
        monitor_viewed_after_probe = True
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
        continue

    # Check if all conditions are stable
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[1] > 0
        and measured_values[1] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default to monitoring if nothing is urgent
    print(16)  # ViewMonitor