airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Handle quick emergency interventions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Complete initial ABCDE assessments
    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            if events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:
                airway_confirmed = True
            continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            if any(events[7:15] > 0):
                breathing_assessed = True
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            if events[16] > 0 or events[17] > 0:
                circulation_checked = True
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            if events[21] > 0 or events[22] > 0 or events[23] > 0:
                disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Work with device dependencies for accurate measurements.
    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # After confirming the SatsProbe is used, ensure oxygen is adequate
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if not bpCuffUsed:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    # Assess and monitor blood pressure continuously until stabilized
    if measured_times[4] != 0 and measured_values[4] < 60:
        print(38)  # TakeBloodPressure
        continue

    # Finish if all conditions for stable John are met
    if all(
        [
            measured_times[5] > 0 and measured_values[5] >= 88,
            measured_times[6] > 0 and measured_values[6] >= 8,
            measured_times[4] > 0 and measured_values[4] >= 60,
        ]
    ):
        print(48)  # Finish
        break

    # Default action if no other conditions are met
    print(0)  # DoNothing