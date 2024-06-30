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

    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Immediate life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Initial ABCDE assessment
    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1:  # AirwayClear
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue

        if not breathing_assessed:
            if not satsProbeUsed:
                print(25)  # UseSatsProbe
                satsProbeUsed = True
                continue
            breathing_assessed = True

        if not circulation_checked:
            print(27)  # UseBloodPressureCuff
            circulation_checked = True
            continue

        if not disability_checked:
            if events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1:  # AVPU Checks
                disability_checked = True
            else:
                print(6)  # ExamineDisability
                continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Check stabilization criteria
    if initial_assessments_done:
        finish_conditions_met = (
            measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
            and measured_times[4] > 0
            and measured_values[4] >= 60
        )
        if finish_conditions_met:
            print(48)  # Finish
            break

        # Additional checks and adjustments
        if measured_times[5] == 0 or measured_values[5] < 88:
            if not satsProbeUsed:
                print(25)  # UseSatsProbe
                satsProbeUsed = True
                continue
        if measured_times[4] == 0 or measured_values[4] < 60:
            print(27)  # UseBloodPressureCuff
            continue