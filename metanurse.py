while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Immediate Critical Interventions
    if times_recent_measure[5] > 0:
        if values[5] < 65:
            print(17)  # StartChestCompression if sats critically low
            continue

    if times_recent_measure[4] > 0:
        if values[4] < 20:
            print(17)  # StartChestCompression if MAP critically low
            continue

    # ABCDE Assessment & Interventions
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask immediately
        continue

    # Checking events and deciding on actions based on ABCDE protocol
    if events[3] < 0.5:  # Check Airway if no recent clear indicator
        print(3)  # ExamineAirrigate
        continue

    if events[0] < 0.5:  # Low relevance of response verbal
        print(8)  # ExamineResponse
        continue

    # General Monitoring and Stabilization
    print(16)  # ViewMonitor as fallback action
    if all(
        v >= threshold for v, threshold in zip(values, [88, 60])
    ):  # Simplified condition
        print(48)  # Finish
        break