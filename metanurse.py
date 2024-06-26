while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    if events[3] <= 0.1:
        print(3)  # ExamineAirway
    elif events[7] > 0.1 or (events[6] <= 0.1 and measurements[6] < 8):
        print(29)  # Use Bag Valve Mask
    elif events[17] > 0.1:
        print(17)  # StartChestCompression
    elif times[5] > 0 and measurements[5] < 65:
        print(17)  # StartChestCompression
    elif times[5] > 0 and measurements[5] < 88:
        print(30)  # Use Non Rebreather Mask
    elif times[4] > 0 and measurements[4] < 60:
        print(15)  # Give Fluids
    else:
        stabilized = (
            times[5] > 0
            and measurements[5] >= 88
            and times[4] > 0
            and measurements[4] >= 60
            and times[6] > 0
            and measurements[6] >= 8
        )
        if stabilized:
            print(48)  # Finish - John is stabilized
            break
        else:
            print(0)  # DoNothing