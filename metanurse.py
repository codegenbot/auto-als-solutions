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

    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        compressions_started = True
        print(17)  # StartChestCompression
        continue

    if compressions_started:
        print(0)  # DoNothing, assume CPR continues automatically
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1:  # AirwayClear event check
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue

        if not breathing_confirmed:
            print(4)  # ExamineBreathing
            continue

        if not circulation_confirmed:
            print(5)  # ExamineCirculation
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    if initial_assessments_done:
        if (measured_times[5] > 0 and measured_values[5] < 88) and not sats_probe_used:
            print(25)  # UseSatsProbe
            sats_probe_used = True
            continue

        if (
            (measured_times[5] > 0 and measured_values[5] >= 88)
            and (measured_times[6] > 0 and measured_values[6] >= 8)
            and (measured_times[4] > 0 and measured_values[4] >= 60)
        ):
            print(48)  # Finish
            break

        # Default action to keep examining if still not stabilized
        if not airway_confirmed:
            print(3)  # ExamineAirway
        elif not breathing_confirmed:
            print(4)  # ExamineBreathing
        elif not circulation_confirmed:
            print(5)  # ExamineCirculation
        else:
            print(0)  # DoNothing