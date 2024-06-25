while True:
    try:
        observations = input().strip().split()
        events = observations[:39]
        times = observations[39:46]
        measurements = observations[46:]

        if float(measurements[5]) < 65 or float(measurements[4]) < 20:
            print(17)  # StartChestCompression
        elif any(float(e) > 0 for e in events[6:8]):
            print(29)  # UseBagValveMask
        elif float(measurements[5]) >= 88 and float(measurements[4]) >= 60 and float(measurements[6]) >= 8:
            print(48)  # Finish
        else:
            if float(times[0]) == 0:
                print(3)  # ExamineAirway
            elif float(times[4]) == 0:
                print(38)  # TakeBloodPressure
            elif float(times[5]) == 0:
                print(25)  # UseSatsProbe
            elif float(measurements[5]) < 88:
                print(30)  # UseNonRebreatherMask
            elif float(measurements[4]) < 60:
                print(15)  # GiveFluids
            elif float(measurements[6]) < 8:
                print(4)  # ExamineBreathing
    except EOFError:
        break