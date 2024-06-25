while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Parsing inputs
        event_types = observations[:39]
        measurement_timeliness = observations[39:46]
        measurements = observations[46:]

        airway_clear = event_types[3]
        breathing_none = event_types[7]
        measured_resps_relevance = measurement_timeliness[6]
        measured_resps = measurements[6]
        measured_sats_relevance = measurement_timeliness[5]
        measured_sats = measurements[5]
        measured_map_relevance = measurement_timeliness[4]
        measured_map = measurements[4]

        # Critical instant lifesaving checks
        if measured_sats_relevance > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if measured_map_relevance > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Airway management
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue

        # Breathing management
        if breathing_none > 0:
            print(29)  # UseBagValveMask
            continue
        if measured_resps_relevance > 0 and measured_resps < 8:
            print(29)  # UseBagValveMask
            continue

        # Circulation stabilization
        if measured_map_relevance > 0 and measured_map < 60:
            print(15)  # GiveFluids
            continue

        # Check oxygenation and apply oxygen if needed
        if measured_sats_relevance > 0 and measured_sats < 88:
            if airway_clear > 0:
                print(30)  # UseNonRebreatherMask
            else:
                print(3)  # ExamineAirway
            continue

        # If all stabilizing conditions are met
        print(48)  # Finish
        break

    except EOFError:
        break