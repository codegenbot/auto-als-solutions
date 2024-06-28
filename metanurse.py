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
    if not airway_clear_confirmed or events[3] <= 0.5:  # Airway not clear or not checked
        print(3)  # ExamineAirway
        step_count += 1
        continue
    elif events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5:  # Airway obstructions exist
        if events[6] > 0.5:  # AirwayTongue obstruction
            print(37)  # PerformJawThrust
        else:
            print(31)  # UseYankeurSuctionCatheter
        step_count += 1
        continue
    else:
        airway_clear_confirmed = True

    # Breathing assessment and intervention
    if events[7] > 0.5:  # BreathingNone detected
        print(29)  # UseBagValveMask
        step_count += 1
        continue
    elif measured_times[5] > 0 and measured_values[5] < 88:
        print(30) # UseNonRebreatherMask
        step_count += 1
        continue
    elif measured_times[1] > 0 and measured_values[1] < 8:
        print(29)  # UseBagValveMask
        step_count += 1
        continue

    # Circulation assessment and intervention
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        step_count += 1
        continue
    elif events[17] > 0.5:  # RadialPulseNonPalpable
        print(5)  # ExamineCirculation
        step_count += 1
        continue

    # Disability checks
    if max(events[21:24]) <= 0.5:  # No clear AVPU status
        print(6)  # ExamineDisability
        step_count += 1
        continue

    # Exposure evaluations
    if max(events[26:]) <= 0.5:  # No exposure checks done
        print(7)  # ExamineExposure
        step_count += 1
        continue

    # Stabilization checks
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
    step_contact += 1