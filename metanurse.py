airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessions_done = False
satsProbeUsed = False
sats_checked = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if events[7] > 0.1:  # BreathingNone
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        continue

    if not circulation_checked:
        print(5)  # ExamineCirculation
        continue

    if not sats_checked:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        sats_checked = True
        continue

    if measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check stabilization qualifications
    if (
        measured_values[4] >= 60
        and measured_values[5] >= 88
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break