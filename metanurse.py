while True:
    try:
        observations = input().strip().split()
        events = observations[:39]
        times = observations[39:46]
        measurements = observations[46:]

        if float(measurements[5]) < 65 or float(measurements[4]) < 20:
            print(17)  # StartChestCompression
            continue
        if (
            float(measurements[5]) >= 88
            and float(measurements[4]) >= 60
            and float(measurements[6]) >= 8
        ):
            print(48)  # Finish
            continue

        # Examine order based on priority and measurements
        if float(times[0]) == 0 or float(events[6]) > 0 or float(events[7]) > 0:
            print(3)  # ExamineAirway
        elif float(times[1]) == 0:
            print(4)  # ExamineBreathing
        elif float(times[2]) == 0 or float(measurements[4]) < 60:
            print(5)  # ExamineCirculation
        elif float(times[3]) == 0:
            print(6)  # ExamineDisability
        elif float(times[4]) == 0:
            print(7)  # ExamineExposure
        elif float(measurements[5]) < 88:
            print(30)  # UseNonRebreatherMask
        elif float(measurements[6]) < 8:
            print(29)  # UseBagValveMask
        else:
            print(0)  # DoNothing
    except EOFError:
        break