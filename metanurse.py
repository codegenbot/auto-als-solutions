airway_clear_confirmed = False
step_count = 0

while stepCounter < 350:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        step_count += 1
        continue

    # Airway assessment and interventions
    if not airway_clear_confirmed:
        if events[3] > 0.5:  # AirwayClear confirmed
            airway_clear_confirmed = True
        else:
            print(3)  # ExamineAirway
            step_count += 1
            continue

    if (
        events[1] > 0.5
        or events[2] > 0.5
        or events[4] > 0.5
        or events[5] > 0.5
        or events[6] > 0.5
    ):  # Airway problems
        print(35)  # PerformAirwayManoeuvres
        step_count += 1
        continue

    # Breathing assessment and interventions
    if events[7] > 0.5 or events[8] > 0.5:  # Severe breathing issues
        print(29)  # UseBagValveMask
        step_count += 1
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        step_count += 1
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        step_count += 1
        continue

    if sum(events[8:14]) == 0:  # No detailed breathing checks done recently
        print(4)  # ExamineBreathing
        step_count += 1
        continue

    # Circulation assessment and interventions
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        step_count += 1
        continue

    if events[16] == 0 and events[17] > 0.5:  # RadialPulseNonPalpable
        print(5)  # ExamineCirculation
        step_count += 1
        continue

    # Disability checks and Exposure
    if events[21] == 0 and events[22] == 0 and events[23] == 0:  # AVPU not checked
        print(6)  # ExamineDisability
        step_count += 1
        continue

    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        step_count += 1
        continue

    # Check for stabilization
    if airway_clear_confirmed:
        if measured_times[5] > 0 and measured_values[5] >= 88:
            if measured_times[6] > 0 and measured_values[6] >= 8:
                if measured_times[4] > 0 and measured_values[4] >= 60:
                    print(48)  # Finish
                    break

    # Default action if no specific action needed
    print(16)  # ViewMonitor
    step_count += 1