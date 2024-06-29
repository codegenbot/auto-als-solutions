airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
initial_assessments_done = False
steps = 0


def critical_conditions(events, measured_times, measured_values):
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        return 29  # UseBagValveMask

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        return 17  # StartChestCompression
    return None


while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    critical_action = critical_conditions(events, measured_times, measured_values)
    if critical_action is not None:
        print(critical_action)
        continue

    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0.1:  # AirwayClear event is recently true
            airway_confirmed = True
        continue

    if airway_confirmed and not breathing_assessed:
        print(4)  # ExamineBreathing
        if events[10] > 0.1:  # EqualChestExpansion event is recently true
            breathing_assessed = True
        continue

    if airway_confirmed and breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
        if (
            events[16] > 0.1 or events[17] > 0.1
        ):  # RadialPulsePalpable or RadialPulseNonPalpable
            circulation_checked = True
        continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and not disability_checked
    ):
        print(6)  # ExamineDisability
        if (
            events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1
        ):  # AVPU_A or AVPU_U or AVPU_V
            disability_checked = True
        continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
        if not initial_assessments_done:
            print(7)  # ExamineExposure
            initial_assessments_done = True
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

    if measured_times[5] == 0 or measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
    elif measured_times[4] == 0 or measured_values[4] < 60:
        print(15)  # GiveFluids
    else:
        print(16)  # ViewMonitor