airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
initial_assessments_done = False
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

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            if events[3] > 0.1:  # AirwayClear
                airway_confirmed = True
            continue
        if not breathing_assessed:
            print(4)  # ExamineBreathing
            if events[10] > 0.1:  # BreathingEqualChestExpansion
                breathing_assessed = True
            continue
        if not circulation_checked:
            print(5)  # ExamineCirculation
            if (
                events[16] > 0.1 or events[17] > 0.1
            ):  # RadialPulsePalpable or RadialPulseNonPalpable
                circulation_checked = True
            continue
        if not disability_checked:
            print(6)  # ExamineDisability
            if (
                events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1
            ):  # AVPU_A, AVPU_U, AVPU_V
                disability_checked = True
            continue

        if (
            airway_confirmed
            and breathing_assessed
            and circulation_checked
            and disability_checked
        ):
            initial_assessments_done = True
            print(7)  # ExamineExposure
            continue

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
        else:
            if measured_times[5] == 0 or measured_values[5] < 88:
                print(30)  # UseNonRebreatherMask
            elif measured_times[4] == 0 or measured_values[4] < 60:
                print(14)  # UseVenflonIVCatheter
                print(15)  # GiveFluids
            else:
                print(16)  # ViewMonitor