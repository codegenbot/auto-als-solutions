while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Immediate critical actions for life-threatening conditions
    # Checking for zero pulse or any condition indicating cardiac arrest
    if (
        times_recent_measure[0] > 0 and values[0] < 30
    ):  # Hypothetical check for extremely low heart rate
        print(17)  # StartChestCompression
        continue

    if times_recent_measure[5] > 0:
        if values[5] < 65:
            print(17)  # StartChestCompression for severe low sats
            continue
        elif values[5] < 88:
            print(30)  # UseNonRebreatherMask for low sats
            continue

    if times_recent_measure[4] > 0:
        if values[4] < 20:
            print(17)  # StartChestCompression for critical low MAP
            continue
        elif values[4] < 60:
            print(15)  # GiveFluids for low MAP
            continue

    # Airway management enhancement by repeated checks and actions
    if events[3] + events[4] + events[5] < 0.5:
        print(3)  # ExamineAirway if no clear airway event
        continue

    # Breathing and ventilation management
    if events[7] > 0.5 or (times_recent_measure[6] > 0 and values[6] < 8):
        print(29)  # UseBagValveMask for insufficient breathing
        continue

    # Regular assessment of vital signs using tools to update observation relevance
    if (
        times_recent_measure[5] == 0
        or times_recent_measure[4] == 0
        or times_recent_measure[6] == 0
    ):
        if times_recent_measure[5] == 0:
            print(25)  # UseSatsProbe
        if times_recent_measure[4] == 0:
            print(27)  # UseBloodPressureCuff
        if times_recent_measure[6] == 0:
            print(5)  # ExamineCirculation
        continue

    # Exhaustive auxiliary systems checkup if previous immediate remedies don't stabilize the patient
    print(4)  # ExamineBreathing
    print(6)  # ExamineDisability
    print(7)  # ExamineExposure

    # Final check if conditions are met for stabilisation
    if (
        times_recent_measure[5] > 0
        and values[5] >= 88
        and times_recent_measure[6] > 0
        and values[6] >= 8
        and times_recent_measure[4] > 0
        and values[4] >= 60
    ):
        print(48)  # Finish if all conditions are stable
        break

    # Default action to gather more information until a clear path is determined
    print(16)  # ViewMonitor, default action when unsure