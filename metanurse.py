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

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Perform initial assessment
    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            continue
        if events[3] > 0:  # AirwayClear
            airway_confirmed = True

        if airway_confirmed and not breathing_assessed:
            print(4)  # ExamineBreathing
            continue
        if (
            events[11] > 0 or events[12] > 0 or events[13] > 0 or events[14] > 0
        ):  # Any breathing issues event
            breathing_assessed = True
            print(29)  # UseBagValveMask
            continue

        if breathing_assessed and not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        if circulation_checked and not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if disability_checked and not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            initial_assessments_done = True
            continue

    # Use Sats Probe only once after full initial assessment
    if not satsProbeUsed and initial_assessments_done:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # Treat specific conditions based on observations
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if not bpCuffUsed and initial_assessments_done:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check complete stabilization and finish
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