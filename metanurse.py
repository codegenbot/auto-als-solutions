airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
monitorViewed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Implement immediate life-saving checks
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check and use sats probe if not already done effectively
    if not satsProbeUsed or monitorViewed:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        monitorViewed = False
        continue

    # View monitor to get readings
    if satsProbeUsed and not monitorViewed:
        print(16)  # ViewMonitor
        monitorViewed = True
        continue

    # Airway check
    if not airway_confirmed:
        print(3)  # ExamineAirway
        airway_confirmed = True
        continue

    if not breathing_assessed:
        if events[10] > 0:  # BreathingEqualChestExpansion observed
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
            continue

    if not circulation_checked:
        if (
            events[16] > 0 or events[17] > 0
        ):  # Radial Pulse Palpable or Non-Palpable observed
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    if not disability_checked:
        if events[21] > 0 or events[22] > 0:  # AVPU_U or AVPU_V observed
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Check if all stabilization criteria are met
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

    print(0)  # DoNothing as a default action if no other conditions trigger