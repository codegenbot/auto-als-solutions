while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_events[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway check and management
    if (
        events[3] < 0.5 and events[4] == 0 and events[5] == 0 and events[6] == 0
    ):  # Airway unclear
        print(3)  # ExamineAirway
        continue
    elif (
        events[4] > 0 or events[5] > 0 or events[6] > 0
    ):  # Obstructions like vomit, blood, tongue
        print(35)  # PerformAirwayManoeuvres
        continue

    # Breathing support
    if events[7] > 0.5:  # Severe breathing issues
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
    if events[22] > 0.5 or events[23] > 0.5:  # Response level check
        print(6)  # ExamineDisability
        continue

    # Exposure examination
    if events[26] > 0.5:  # Check for systemic problems
        print(7)  # ExamineExposure
        continue

    # Regular monitoring and reassessment
    if events[25] == 0 and events[26] == 0 and events[27] == 0:  # Normal conditions
        print(16)  # ViewMonitor
        continue

    # Decision to finish
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