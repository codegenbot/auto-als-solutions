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

    # Airway check and management
    if not events[3]:  # Airway unclear
        print(3)  # ExamineAirway
        continue
    elif (
        events[4] > 0 or events[5] > 0 or events[6] > 0
    ):  # Obstructions like vomit, blood, tongue
        print(35)  # PerformAirwayManoeuvres
        continue

    # Breathing support
    if events[7] > 0:  # Severe breathing issues
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:  # Low oxygen saturation
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation check
    if measured_times[4] > 0 and measured_values[4] < 60:  # Low mean arterial pressure
        print(15)  # GiveFluids
        continue

    # Disability assessment
    if events[21] > 0 or events[22] > 0:  # Response level check
        print(6)  # ExamineDisability
        continue

    # Exposure examination
    if events[26] > 0:  # Check for systemic problems
        print(7)  # ExamineExposure
        continue

    # If all vital perimeters are normal and sustained, prepare to finish
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

    # Default action if none of the above conditions met
    print(16)  # ViewMonitor