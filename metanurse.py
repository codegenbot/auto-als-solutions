while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        if measurements[5] < 65 or measurements[4] < 20:
            print(17)  # StartChestCompression
        elif any([events[i] > 0 for i in [7]]):  # Checking for BreathingNone
            print(29)  # UseBagValveMask
        elif measurements[5] >= 88 and measurements[4] >= 60 and measurements[6] >= 8:
            print(48)  # Finish
        else:
            if times[0] == 0:
                print(3)  # ExamineAirway
            elif times[4] == 0:
                print(38)  # TakeBloodPressure
            elif times[5] == 0:
                print(25)  # UseSatsProbe
            elif measurements[5] < 88:
                print(30)  # UseNonRebreatherMask
            elif measurements[4] < 60:
                print(15)  # GiveFluids
            elif measurements[6] < 8:
                print(4)  # ExamineBreathing

    except EOFError:
        break