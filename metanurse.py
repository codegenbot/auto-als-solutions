airway_clear_confirmed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway assessment and interventions
    if not airway_clear_confirmed or events[3] < 0.5:  # AirwayClear confirmed check
        print(3)  # ExamineAirway
        continue
    else:
        airway_clear_confirmed = True

    # Checking if airway problem persists
    if events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5:
        print(35)  # PerformAirwayManoeuvres
        continue

    # Breathing assessment and intervention
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[1] > 0 and measured_values[1] < 8:
        print(29)  # UseBagValueMask
        continue

    # Breathing checks
    if any(events[8:14]):
        print(4)  # ExamineBreathing
        continue

    # Circulation assessment and intervention
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if events[16] > 0.5 and events[17] < 0.5:  # RadialPulseNonPalpable
        print(5)  # ExamineCirculation
        continue

    # Disability checks
    if events[21] == 0 and events[22] == 0 and events[23] == 0:  # AVPU not checked
        print(6)  # ExamineDisability
        continue

    # Exposure checks
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Checking stabilization criteria
    if (
        airway_clear_confirmed
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[1] > 0
        and measured_values[1] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default action if no specific condition matched
    print(16)  # ViewMonitor