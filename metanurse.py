airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
emergency_intervention_performed = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical condition handling
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # ABCDE assessments
    if not airway_confirmed:
        if events[3] > 0:  # AirwayClear
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
        continue
    elif not breathing_assessed:
        if events[12] > 0:  # BreathingEqualChestExpansion
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
        continue
    elif not circulation_checked:
        if events[17] >= 0.5 or events[16] >= 0.5:  # RadialPulse palpable
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
        continue
    elif not disability_checked:
        if events[25] > 0:  # PupilsNormal or any AVPU response
            disability_checked = True
        else:
            print(6)  # ExamineDisability
        continue
    elif not exposure_checked:
        if events[26] > 0:  # ExposureRash or any other
            exposure_checked = True
        else:
            print(7)  # ExamineExposure
        continue

    # Monitor and reassess regularly
    if measured_times[4] <= 0:  # Blood pressure not measured recently
        print(27)  # UseBloodPressureCuff
    elif measured_times[5] <= 0:  # Sats not measured recently
        print(25)  # UseSatsProbe
    elif emergency_intervention_performed and (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break
    else:
        print(16)  # ViewMonitor