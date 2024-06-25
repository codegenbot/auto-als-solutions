while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))
        measured_sats = observations[46]
        measured_map = observations[45]

        if measured_sats < 65 or measured_map < 20:
            print(17)  # StartChestCompression
        elif measured_sats < 88 or measured_map < 60:
            if observations[3] > 0:  # AirwayClear
                print(30)  # UseNonRebreatherMask
            else:
                print(3)  # ExamineAirway
        else:
            print(48)  # Finish
    except EOFError:
        break