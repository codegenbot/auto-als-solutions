airway_clear_confirmed = False
while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_clear_confirmed:
        if events[3] > 0.5:
            airway_clear_confirmed = True
        else:
            print(3)
            continue

    # Airway assessment and interventions
    if any([events[i] > 0.5 for i in [1, 2, 4, 5, 6]]):  # Airway problems
        print(35)  # PerformAirwayManoeuvres
        continue

    # Breathing assessment and interventions
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    elif measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    elif measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation interventions
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Disability assessment
    if all([events[i] == 0 for i in range(25, 29)]):  # No pupil reaction
        print(6)  # ExamineDisability
        continue

    # Exposure check
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Stabilization check
    if (
        airway_clear_confirmed
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor