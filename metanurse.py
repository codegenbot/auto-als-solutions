while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Critical immediate actions for life-threatening conditions
    if times_recent_measure[5] > 0:
        if values[5] < 65:
            print(17)  # StartChestCompression for critical low sats
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

    # Check Airway
    if (
        events[3] + events[4] + events[5] < 0.1 and events[3] == 0
    ):  # Checking if airway is not clear
        print(3)  # ExamineAirway
        continue

    # Check Breathing
    breathing_issues = (
        events[7] > 0 or events[8] > 0 or events[9] > 0
    )  # BreathingNone, BreathingSnoring, BreathingSeeSaw
    if breathing_issues or (times_recent_measure[6] > 0 and values[6] < 8):
        print(29)  # UseBagValveMask for insufficient breathing
        continue

    # Check Circulation
    if not events[16] > 0:  # RadialPulsePalpable
        print(5)  # ExamineCirculation
        continue

    # Check Disability (consciousness)
    if not (
        events[21] > 0 or events[22] > 0
    ):  # AVPU_U or AVPU_V (not optimal consciousness)
        print(6)  # ExamineDisability
        continue

    # Check Exposure
    if not (
        events[25] > 0 or events[26] > 0 or events[27] > 0
    ):  # No obvious signs from exposure examined
        print(7)  # ExamineExposure
        continue

    # Final check if stabilization criteria are met
    stabilized = (
        events[2] > 0
        and times_recent_measure[5] > 0  # AirwayClear
        and values[5] >= 88
        and times_recent_measure[6] > 0
        and values[6] >= 8
        and times_recent_measure[4] > 0
        and values[4] >= 60
    )

    if stabilized:
        print(48)  # Finish if all conditions are stable
        break

    # Default action to gather more information
    print(16)  # ViewMonitor, default safe action