airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
sats_probe_used = False
breathing_drawer_opened = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not breathing_drawer_opened:
        print(19)  # OpenBreathingDrawer
        breathing_drawer_opened = True
        continue

    if not sats_probe_used and breathing_drawer_opened:
        print(25)  # UseSatsProbe
        sats_probe_used = True
        continue

    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    if measured_times[5] > 0 and measured_values[5] >= 88 and measured_times[6] > 0 and measured_values[6] >= 8 and measured_times[4] > 0 and measured_values[4] >= 60:
        print(48)  # Finish
        break

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            continue

        initial_assessments_done = True

    print(0)  # DoNothing as last resort