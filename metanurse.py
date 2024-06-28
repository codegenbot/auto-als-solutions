airway_clear_confirmed = False
step_count = 0

while step_count < 350:
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
        events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5
    ):  # Airway obstruction problems
        print(36)  # PerformHeadTiltChinLift
        step_count += 1
        continue

    # Breathing assessment and intervention
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        step_count += 1
        continue
    if measured_times[5] <= 0 or measured_values[5] < 88:
        print(25)  # UseSatsProbe
        step_count += 1
        continue
    if measured_times[6] <= 0 or measured_values[6] < 8:
        print(4)  # ExamineBreathing
        step_count += 1
        continue

    # Circulation assessment and intervention
    if measured_times[4] <= 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        step_count += 1
        continue

    if events[16] == 0 and events[17] > 0.5:  # RadialPulseNonPalpable
        if measured_times[4] == 0 or measured_values[4] < 60:
            print(15)  # GiveFluids
        else:
            print(5)  # ExamineCirculation
        step_count += 1
        continue

    # Disability checks
    if events[21] == 0 and events[22] == 0 and events[23] == 0:  # AVPU not clear
        print(6)  # ExamineDisability
        step_count += 1
        continue

    # Exposure checks
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        step_count += 1
        continue

    # Checking stabilization criteria
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

    # Default action if no specific condition matched
    print(16)  # ViewMonitor
    step_count += 1