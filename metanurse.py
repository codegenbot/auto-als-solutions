while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-threatening conditions checks
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Airway checks
    if events[3] < 0.5 and all(events[i] < 0.5 for i in range(4, 7)):  # Airway issues
        if events[3] == 0:
            print(3)  # ExamineAirway
        elif events[5]:  # AirwayVomit
            print(31)  # UseYankeurSucionCatheter
        continue

    # Breathing checks
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:  # Low oxygen saturation
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:  # Low respiratory rate
        print(29)  # UseBagValveMask
        continue

    # Circulation checks
    if measured_times[4] > 0 and measured_values[4] < 60:  # Low mean arterial pressure
        print(15)  # GiveFluids
        continue

    # Disability and Exposure might be assessed here in a full implementation
    # E.g., check AVPU, exposure (signs of trauma, rashes, etc.)

    # Check stability
    stable_conditions = (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    )
    if stable_conditions:
        print(48)  # Finish
        break

    # If no critical actions required, loop the primary exams (ABCDE)
    if events[3] < 0.5:
        print(3)  # ExamineAirway
    elif max(measured_times[5], measured_times[6], measured_times[4]) == 0:
        print(16)  # ViewMonitor
    else:
        print(4)  # ExamineBreathing