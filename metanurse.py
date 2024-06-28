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
    if airway_clear_confirmed:
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
    else:
        if events[3] > 0.5:  # AirwayClear confirmed
            airway_clear_confirmed = True
        else:
            print(3)  # ExamineAirway
            step_count += 1
            continue

    # Breathing assessment and intervention
    if measured_times[1] == 0:  # No recent breathing data
        print(4)  # ExamineBreathing
        step_count += 1
        continue
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        step_count += 1
        continue
    if measured_times[5] == 0 or measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        step_count += 1
        continue
    if measured_times[6] == 0 or measured_values[6] < 8:
        print(29)  # UseBagValveMask
        step_count += 1
        continue

    # Circulation assessment and intervention
    if measured_times[4] == 0 or measured_values[4] < 60:
        print(15)  # GiveFluids
        step_count += 1
        continue
    if events[16] == 0 and events[17] > 0.5:  # Pulse not palpable
        print(5)  # ExamineCirculation
        step_count += 1
        continue

    # Disability checks
    if events[21:24] == [0] * 3:  # No AVPU information
        print(6)  # ExamineDisability
        step_count += 1
        continue

    # Exposure checks
    if events[26] > 0.5:  # Possible peripheral shutdown
        print(7)  # ExamineExposure
        step_count += 1
        continue

    # Ensure vitals are measured
    if measured_times[0] == 0:  # Heart rate not measured
        print(26)  # UseAline
    elif measured_times[1] == 0:  # Respiratory rate not measured
        print(25)  # UseSatsProbe
    elif measured_times[4] == 0:  # MAP not measured
        print(27)  # UseBloodPressureCuff
    else:
        print(16)  # ViewMonitor

    # Increment step count, per loop iteration
    step_count += 1