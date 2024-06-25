while True:
    try:
        observations = input().strip().split()
        events = observations[:39]
        times = observations[39:46]
        measurements = observations[46:]

        # Immediate life-threatening conditions
        if float(measurements[5]) < 65 or float(measurements[4]) < 20:
            print(17)  # StartChestCompression
            continue

        # Check if Airway observations have been recently made, if not, make them
        if float(events[6]) == 0 and float(events[5]) == 0 and float(events[4]) == 0 and float(events[3]) == 0:
            print(3)  # ExamineAirway
            continue

        # Airway management based on observations
        if float(events[3]) > 0:  # AirwayClear
            print(0)  # DoNothing as airway is clear
        elif float(events[4]) > 0 or float(events[5]) > 0:  # AirwayVomit or AirwayBlood
            print(31)  # UseYankeurSucionCatheter
            continue
        elif float(events[6]) > 0:  # AirwayTongue
            print(32)  # UseGuedelAirway
            continue

        # If Breathing observations are not up to date
        if float(times[6]) == 0:
            print(4)  # ExamineBreathing
            continue

        # Ensure adequate breathing
        if float(measurements[6]) < 8:
            print(29)  # UseBagValveMask
            continue

        # Monitor steady sat levels
        if float(times[5]) == 0:
            print(25)  # UseSatsProbe
            continue
        if float(measurements[5]) < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # Ensure Circulation is adequate
        if float(times[4]) == 0:
            print(38)  # TakeBloodPressure
            continue
        if float(measurements[4]) < 60:
            print(15)  # GiveFluids
            continue

        # If all critical parameters are stable
        if float(measurements[5]) >= 88 and float(measurements[6]) >= 8 and float(measurements[4]) >= 60:
            print(48)  # Finish
            continue

    except EOFError:
        break