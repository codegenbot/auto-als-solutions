while True:
    try:
        observations = input().strip().split()
        events = observations[:39]
        times = observations[39:46]
        measurements = observations[46:]

        if float(measurements[5]) < 65 or float(measurements[4]) < 20:
            print(17)  # StartChestCompression
        elif float(measurements[5]) < 88 or float(measurements[4]) < 60 or float(measurements[6]) < 8:
            if float(times[4]) == 0:
                print(38)  # TakeBloodPressure
            elif float(times[5]) == 0:
                print(25)  # UseSatsProbe
            elif float(times[6]) == 0:
                print(4)  # ExamineBreathing
            else:
                if float(measurements[5]) < 88:
                    print(30)  # UseNonRebreatherMask
                if float(measurements[4]) < 60:
                    print(15)  # GiveFluids
                if float(measurements[6]) < 8:
                    print(29)  # UseBagValveMask
        else:
            print(48)  # Finish
    except EOFError:
        break