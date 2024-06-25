while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Parsing inputs
        event_types = observations[:39]
        measurement_timeliness = observations[39:46]
        measurements = observations[46:]

        # Unpack vital sign measurements
        airway_clear = event_types[3]
        breathing_none = event_data[7]
        measured_resps_relevance = measurement_data[6]
        measured_resps = measurements[6]
        measured_sats_relevance = measurement_timeliness[5]
        measured_sats = measurements[5]
        measured_map_relevance = measurement_timeliness[4]
        measured_map = measurements[4]

        # Check immediate life-threatening condition
        if measured_sats_relevance > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if measured_map_relevance > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Initial Examination for complete assessment
        print(3)  # ExamineAirway
        print(4)  # ExamineBreathing
        print(5)  # ExamineCirculation
        print(6)  # ExamineDisability
        print(7)  # ExamineExposure

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

        # Oxygenation check and correction
        if measured_sats_relevance > 0 and measured_sats < 88:
            if airway_clear > 0:
                print(30)  # UseNonRebreatherMask
            else:
                print(3)  # ExamineAirway
            continue

        # All stabilization conditions met
        print(48)  # Finish
        break

    except EOFJsonRe:
        break