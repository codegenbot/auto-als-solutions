airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Handle critical situations
    if events[7] > 0 or (
        measured_times[6] > 0 and measured_values[6] < 8
    ):  # BreathingNone or very low resps
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Assessment Flow
    if not initial_assessments_done:
        if not airway_confirmed:
            if (
                events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0
            ):  # Any Airway check
                airway_confirmed = True
                print(
                    31 if events[4] > 0 or events[5] > 0 else 3
                )  # Yankeur if Vomit/Blood else Examine
                continue
            print(3)  # ExamineAirway
            continue

        if not breathing_assessed:
            breathing_assessed = True
            print(4)  # ExamineBreathing
            continue

        if not circulation_checked:
            circulation_checked = True
            print(5)  # ExamineCirculation
            continue

        if not disability_checked:
            disability_checked = True
            print(6)  # ExamineDisability
            continue

        if not exposure_checked:
            exposure_checked = True
            print(7)  # ExamineExposure
            continue

        initial_assessments_done = True

    # Application of tools and measurements
    if not satsProbeUsed:
        print(
            25 if steps == 1 else 19
        )  # Use Sats Probe initially or Open Breathing Drawer
        satsProbeUsed = True
        continue

    if (measured_times[5] == 0 or measured_values[5] < 88) and not events[
        7
    ]:  # Low Sats and no BreathingNone
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    # Final condition to finish
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

    print(0)  # DoNothing if no action determined