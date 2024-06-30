airway_confirmed = False
breathing_confirmed = False
circulation_confirmed = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
sats_probe_used = False
steps = 0
compressions_started = False

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if events[3] > 0.1:  # AirwayClear event check
        airway_confirmed = True

    if (
        events[3] == 0 and not airway_confirmed
    ):  # No AirwayClear event and airway not confirmed
        print(3)  # ExamineAirway
        continue

    if events[5] > 0.1:  # Breathing problem
        breathing_confirmed = True

    if not breathing_confirmed:
        print(4)  # ExamineBreathing
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        compressions_started = True
        print(17)  # StartChestCompression
        continue

    if compressions_started:
        if (measured_times[5] > 0 and measured_values[5] >= 65) and (
            measured_times[4] > 0 and measured_values[4] >= 20
        ):
            compressions_started = False
        print(0)  # DoNothing, assume CPR continues automatically
        continue

    if (measured_times[5] > 0 and measured_values[5] < 88) and not sats_probe_used:
        print(25)  # UseSatsProbe
        sats_probe_used = True
        continue

    if (
        (measured_times[5] > 0 and measured_values[5] >= 88)
        and (measured_times[1] > 0 and measured_values[1] >= 8)
        and (measured_times[4] > 0 and measured_values[4] >= 60)
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing