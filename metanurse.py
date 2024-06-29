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

    if events[7] >= 0.9 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] == 0:  # AirwayClear not confirmed
                print(3)  # ExamineAirway
                continue
            else:
                airway_confirmed = True

        if not breathing_assessed:
            if events[10] == 0:  # BreathingEqualChestExpansion not confirmed
                print(4)  # ExamineBreathing
                continue
            else:
                breathing_assessed = True

        if not circulation_checked:
            if (
                events[16] == 0 and events[17] == 0
            ):  # RadialPulsePalpable and RadialPulseNonPalpable not confirmed
                print(5)  # ExamineCirculation
                continue
            else:
                circulation_checked = True

        if not disability_checked:
            if (
                events[25] == 0 and events[23] == 0
            ):  # PupilsNormal and PupilsPinpoint not confirmed
                print(6)  # ExamineDisability
                continue
            else:
                disability_checked = True

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    if initial_assessments_done:
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

        if not satsProbeUsed or measured_times[5] == 0 or measured_values[5] < 88:
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue

        if measured_times[4] == 0 or measured_values[4] < 60:
            print(27)  # UseBloodPressureCuff
            continue