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
            print(3)  # ExamineAirway
            if any([events[i] > 0.1 for i in [3, 4, 5]]):  # Airway clear or problems
                airway_confirmed = True
                if events[4] > 0.1:  # Vomit present
                    print(31)  # UseYankeurSuctionCatheter
                    continue
                elif events[5] > 0.1:  # Blood present
                    print(31)  # UseYankeurSuctionCatheter
                    continue
            continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            if any(
                [events[i] > 0 for i in range(7, 15)]
            ):  # Any breathing problem signs
                breathing_assessed = True
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            if any(
                [events[i] > 0.1 for i in [16, 17]]
            ):  # RadialPulsePalpable or RadialPulseNonPalpable
                circulation_checked = True
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            if any([events[i] > 0 for i in [21, 22, 23]]):  # AVPU responses
                disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    if not satsProbeUsed:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if measured_times[5] == 0 or measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
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