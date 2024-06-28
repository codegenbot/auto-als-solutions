while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    if times_recent_measure[5] > 0:
        if values[5] < 65 or events[7] > 0.5:  # Severe hypoxia or no breathing
            print(17)  # StartChestCompression
            continue

    if events[3] > 0:  # Airway clear
        if times_recent_measure[5] > 0 and values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue

    if events[4] + events[5] > 0:  # Airway blocked
        print(31)  # UseYankeurSuctionCatheter
        continue

    if (
        events[3] + events[4] + events[5] < 0.5
    ):  # No recent airway examination or unclear
        print(3)  # ExamineAirway
        continue

    # Check Stability Before Finishing
    if all(
        [
            times_recent_measure[i] > 0 and values[i] >= threshold
            for i, threshold in zip([5, 6, 4], [88, 8, 60])
        ]
    ):
        print(48)  # Finish
        break

    # Default less critical care action
    print(16)  # ViewMonitor to continue obtaining patient status