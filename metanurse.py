while True:
    try:
        observations = input().strip().split()
        events = observations[:39]
        times = observations[39:46]
        measurements = observations[46:]

        has_critical_condition = (
            float(measurements[5]) < 65 or float(measurements[4]) < 20
        )

        if has_critical_condition:
            print(17)  # StartChestCompression
        else:
            sats_relevant = float(times[5]) > 0
            map_relevant = float(times[4]) > 0
            resp_rate_relevant = float(times[6]) > 0

            sats_ok = float(measurements[5]) >= 88
            map_ok = float(measurements[4]) >= 60
            resp_rate_ok = float(measurements[6]) >= 8

            if not (sats_ok and map_ok and resp_rate_ok):
                if not sats_relevant:
                    print(25)  # UseSatsProbe
                elif not map_relevant:
                    print(38)  # TakeBloodPressure
                elif not resp_rate_relevant:
                    print(4)  # ExamineBreathing
                else:
                    if not sats_ok:
                        print(30)  # UseNonRebreatherMask
                    if not map_ok:
                        print(15)  # GiveFluids
                    if not resp_rate_ok:
                        print(29)  # UseBagValveMask
            else:
                print(48)  # Finish
    except EOFError:
        break