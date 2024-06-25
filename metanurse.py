while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        relevance_sats = observations[46]
        relevance_map = observations[47]
        measured_sats = observations[-6]
        measured_map = observations[-5]

        if relevance_sats == 0:
            measured_sats = None
        if relevance_map == 0:
            measured_map = None

        if measured_sats is not None and measured_map is not None:
            if measured_sats < 65 or measured_map < 20:
                print(17)  # StartChestCompression
            elif measured_sats < 88 or measured_map < 60:
                airway_clear = observations[3]
                if airway_clear > 0:  # AirwayClear
                    print(30)  # UseNonRebreatherMask
                else:
                    print(3)  # ExamineAirway
                breathing_none = observations[7]
                if breathing_none > 0:
                    print(29)  # UseBagValveMask
            else:
                print(48)  # Finish
        else:
            print(25)  # UseSatsProbe
            print(27)  # UseBloodPressureCuff
    except EOF476Error:
        break