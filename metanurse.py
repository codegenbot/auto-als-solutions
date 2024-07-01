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

    if events[7] >= 0.7 or (
        measured_times[6] > 0 and measured_values[6] < 8
    ):  # BreathingNone event or low resps rate
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            if events[3] > 0:  # AirwayClear
                airway_confirmed = True
                continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            if set(events[7:15]) - {0}:  # Check all breathing-related events
                breathing_assessed = True
                continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            if (
                events[16] > 0 or events[17] > 0
            ):  # RadialPulsePalpable or RadialPulseNonPalpable
                circulation_checked = True
                continue

        if not disability_checked:
            print(6)  # ExamineDisability
            if any(events[21:24]):  # Check AVPU_A, AVPU_V, AVPU_U
                disability_checked = True
                continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = (
            airway_confirmed
            and breathing_assessed
            and circulation_checked
            and disability_checked
            and exposure_checked
        )

    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        if not satsProbeUsed:
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(38)  # TakeBloodPressure
        continue

    if measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
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

    print(0)  # DoNothing as last resort