airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
sats_checked = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if events[14] >= 0.5:  # severe event like pneumothorax detected
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    if satsProbeUsed:
        if measured_times[5] > 0:
            sats_checked = True
        print(16)  # ViewMonitor
        continue

    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        if not circulation_checked:
            print(20)  # OpenCirculationDrawer
            print(27)  # UseBloodPressureCuff
            circulation_checked = True
            continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check for confirmed airway, breathing assessment, and saturation check
    airway_clear = events[3] > 0.5
    breathing_clear = events[12] > 0.5 or events[13] > 0.5 or events[14] > 0.5

    if not airway_clear:
        print(3)  # ExamineAirway
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    if breathing_assessed and not sats_checked:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        sats_checked = True
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