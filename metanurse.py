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

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            mark_airway_observed = False
            for i in [
                3,
                4,
                5,
                6,
            ]:  # AirwayClear, AirwayVomit, AirwayBlood, AirwayTongue
                if events[i] >= 0.1:
                    mark_airway_observed = True
            if mark_airway_observed:
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue

        if not breathing_assessed:
            mark_breathing_observed = False
            for i in [10, 11, 12, 13, 14]:  # Breathing relevant observations
                if events[i] >= 0.1:
                    mark_breathing_observed = True
            if mark_breathing_observed:
                breathing_assessed = True
                if not satsProbeUsed:
                    print(25)  # UseSatsProbe
                    satsProbeUsed = True
                    continue
            else:
                print(4)  # ExamineBreathing
                continue

        if not circulation_checked:
            mark_circulation_observed = False
            for i in [16, 17]:  # RadialPulsePalpable, RadialPulseNonPalpable
                if events[i] >= 0.1:
                    mark_circulation_observed = True
            if mark_circulation_observed:
                circulation_checked = True
            else:
                print(5)  # ExamineCirculation
                continue

        if not disability_checked:
            mark_disability_observed = False
            for i in [21, 22, 23]:  # AVPU_U, AVPU_V, AVPU_P
                if events[i] >= 0.1:
                    mark_disability_observed = True
            if mark_disability_observed:
                disability_checked = True
            else:
                print(6)  # ExamineDisability
                continue

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

        if measured_times[5] == 0 or measured_values[5] < 88:
            if not satsProbeUsed:
                print(25)  # UseSatsProbe
                satsProbeUsed = True
            else:
                print(30)  # UseNonRebreatherMask
                continue

        if measured_times[4] == 0 or measured_values[4] < 60:
            print(27)  # UseBloodPressureCuff
            continue