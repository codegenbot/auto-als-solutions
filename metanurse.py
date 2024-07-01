airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
satsProbeUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (
        not satsProbeUsed and events[19] == 0
    ):  # Check if BreathingDrawer needs to be opened
        print(19)  # OpenBreathingDrawer
        continue

    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        airway_confirmed = True
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    if measured_times[5] == 0 or measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
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