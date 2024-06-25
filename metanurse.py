while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))
        measured_sats = observations[-1]
        measured_map = observations[-2]
        measured_resps = observations[-3]
        airway_clear_relevance = observations[3]

        if measured_sats < 65 or measured_map < 20:
            print(17)  # StartChestCompression
        elif measured_sats < 88 or measured_map < 60 or measured_resps < 8:
            if airway_clear_relevance == 0:
                print(3)  # ExamineAirway
            elif measured_sats < 88:
                print(30)  # UseNonRebreatherMask
            elif measured_resps < 8:
                print(29)  # UseBagValveMask
            elif measured_map < 60:
                print(15)  # GiveFluids
        else:
            print(48)  # Finish - Patient stabilized
    except EOFError:
        break